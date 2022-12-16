# Fallout RPG Encounter Generator

## What is it?

This device is used to generate random encounters in role playing games, especially in a Fallout Setting, but can be used for any other game.

## Hardware

The code is written to work on a Raspberry Pi Pico (or similar) and a Pimoroni inky.

### The board

A regular Raspberry Pi Pico can be used for this project, or alternatively you can use my personal favorite, a [Pimoroni Pico Lipo](pimoroni.com/picolipo). Just flash the correct firmware that can be found [here](https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md).

### The display

The one I used is the [Pimoroni inky](pimoroni.com/picoinky) to get a use of its three buttons, but the code can be changed to fit the display you have lying around.

## The code

If you flash the correct Pimoroni firmware, you don't need any other additional libraries. Otherwise, you're good enough to add them yourself.

Just upload `main.py` onto your board, and you should be good to go.

### Add your stuff

#### Social encounters

Add your social encounters in the dedicated list.

#### Locations

Dittos

## Usage

Power the board. Press the A button to get a random social encounter. Press the B button to get a location and press C to get a random time and weather update.

## Future work

- [ ] Add english
- [ ] Add other displays