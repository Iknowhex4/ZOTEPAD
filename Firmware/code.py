print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import KeysScanner
# GPIO to key mapping - each line is a new row.
pins = [
    board.SW3,  board.SW7,  board.SW11, board.SW15,
    board.SW2,  board.SW6,  board.SW10, board.SW14,
    board.SW1,  board.SW5,  board.SW9,  board.SW13,
    board.SW0,  board.SW4,  board.SW8,  board.SW12,
]


# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=pins,
            value_when_pressed=False,
            # optional arguments with defaults:
            pull=True,
            interval=0.02, # Matrix sampling interval in ms
            debounce_threshold=None, # Number of samples needed to change state, values greater than 1 enable debouncing. Only applicable for CircuitPython >= 9.2.0
            max_events=64
        )
keyboard = MyKeyboard()


keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    keyboard.go()