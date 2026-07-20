"""Constants for the SuteFoto LED integration."""
from __future__ import annotations

DOMAIN = "sutefoto_led"

CONF_MAC = "mac"

CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"

# Modes
MODE_HSI = "hsi"
MODE_CCT = "cct"
MODE_RGBCW = "rgbcw"
MODE_FX = "fx"

MODES = [MODE_HSI, MODE_CCT, MODE_RGBCW, MODE_FX]

MIN_CCT_KELVIN = 2800
MAX_CCT_KELVIN = 10000

FX_EFFECTS: dict[int, str] = {
    1: "Lightning",
    2: "Police",
    3: "Fire truck",
    4: "Ambulance",
    5: "Fire",
    6: "Fireworks",
    7: "Fault bulb",
    8: "TV",
    9: "RGB Circle",
    10: "Paparazzi",
}
FX_EFFECTS_REVERSE = {v: k for k, v in FX_EFFECTS.items()}

DEFAULT_HUE = 0
DEFAULT_SATURATION = 100
DEFAULT_CCT = 5600
DEFAULT_GM = 0
DEFAULT_FX_EFFECT = 1
DEFAULT_FX_FREQUENCY = 5
DEFAULT_FX_INTENSITY = 100

SIGNAL_STATE_UPDATED = f"{DOMAIN}_state_updated"
