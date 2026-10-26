print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
# GPIO to key mapping - each line is a new row.
pins = [
    board.D0, board.D1, board.D2,
    board.D3, board.D4, board.D5
]
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()


# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=pins,
            value_when_pressed=False
            # optional arguments with defaults:
        )
keyboard = MyKeyboard()

keyboard.modules = [encoder_handler]

# Regular GPIO Encoder
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D8, board.D7, board.D9,), # encoder #1 
    )

encoder_handler.map = [ (( KC.VOLD, KC.VOLU, KC.MUTE),) # Layer 1
                      ]

keyboard.keymap = [
    [KC.RIGHT, KC.X, KC.DOWN, KC.UP, KC.LEFT, KC.Z] 
]

if __name__ == '__main__':
    keyboard.go()