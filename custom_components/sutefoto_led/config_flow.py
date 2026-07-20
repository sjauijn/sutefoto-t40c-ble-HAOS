"""Config flow for SuteFoto LED integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components.bluetooth import (
    BluetoothServiceInfoBleak,
    async_discovered_service_info,
)
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.device_registry import format_mac

from .const import CONF_MAC, DOMAIN


class SuteFotoConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SuteFoto LED."""

    VERSION = 1

    def __init__(self) -> None:
        self._discovered_mac: str | None = None
        self._discovered_name: str | None = None

    async def async_step_bluetooth(
        self, discovery_info: BluetoothServiceInfoBleak
    ) -> ConfigFlowResult:
        """Handle discovery via Bluetooth."""
        await self.async_set_unique_id(format_mac(discovery_info.address))
        self._abort_if_unique_id_configured()
        self._discovered_mac = discovery_info.address
        self._discovered_name = discovery_info.name or discovery_info.address
        self.context["title_placeholders"] = {"name": self._discovered_name}
        return await self.async_step_bluetooth_confirm()

    async def async_step_bluetooth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        if user_input is not None:
            return self.async_create_entry(
                title=self._discovered_name or self._discovered_mac,
                data={CONF_MAC: self._discovered_mac},
            )
        return self.async_show_form(
            step_id="bluetooth_confirm",
            description_placeholders={"name": self._discovered_name},
        )

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initiated by the user, manual MAC entry."""
        errors: dict[str, str] = {}

        discovered: dict[str, str] = {}
        for info in async_discovered_service_info(self.hass, connectable=True):
            name = (info.name or "").upper()
            if name.startswith("ST40") or name.startswith("SUTEFOTO"):
                discovered[info.address] = f"{info.name} ({info.address})"

        if user_input is not None:
            mac = user_input[CONF_MAC].strip().upper()
            await self.async_set_unique_id(format_mac(mac))
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=f"SuteFoto LED ({mac})",
                data={CONF_MAC: mac},
            )

        if discovered:
            schema = vol.Schema(
                {vol.Required(CONF_MAC): vol.In(discovered)}
            )
        else:
            schema = vol.Schema({vol.Required(CONF_MAC): str})

        return self.async_show_form(
            step_id="user", data_schema=schema, errors=errors
        )
