# SuteFoto T40C Light BLE — Home Assistant Integration

Custom Home Assistant integration for the **SuteFoto T40C RGB** professional light
(the one controlled by the [SS LED](https://play.google.com/store/apps/details?id=com.zzcyi.sutudengjv) app), connected directly over Bluetooth LE. 
Protocol reverse engineered from BLE HCI snoop logs.

## Features

- **Light entity** — on/off, brightness, HS color (HSI mode), color temperature (CCT mode)
- **Select: Mode** — switch between HSI / CCT / RGBCW / FX
- **Select: FX Effect** — Lightning, Police, Fire truck, Ambulance, Fire, Fireworks,
  Fault bulb, TV, RGB Circle, Paparazzi
- **Number entities** — Green/Magenta compensation (CCT mode), RGBCW channel levels,
  FX Frequency

## Installation via HACS (custom repository)

1. HACS → Integrations → ⋮ menu (top right) → **Custom repositories**
2. Add this repository URL, category **Integration**
3. Install **SuteFoto LED Light**, restart Home Assistant

## Setup

1. Settings → Devices & services → **Add Integration** → search for "SuteFoto LED"
2. If discovered, select your light from the list; otherwise choose
   **"Enter MAC address manually…"** and type it in (find it with a BLE scanner
   app such as nRF Connect — look for a device named like `ST40CRGB-XXXXXX`)
3. Home Assistant will attempt an actual Bluetooth connection during setup to
   confirm the light is reachable before the integration is added. If this
   fails, make sure the light is not currently connected to the SS LED app.

## Requirements

- Home Assistant instance with Bluetooth support (built-in adapter or a
  [Bluetooth proxy](https://esphome.io/components/bluetooth_proxy.html)) within
  range of the light
- The light must not be actively connected to the [SS LED](https://play.google.com/store/apps/details?id=com.zzcyi.sutudengjv) phone app at setup
  time or while Home Assistant is controlling it (BLE only allows one active
  connection)

## Disclaimer

This is an unofficial, community-reverse-engineered integration and is not
affiliated with or endorsed by SuteFoto.
