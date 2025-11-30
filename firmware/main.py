from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# Main instance of keyboard
keyboard = KMKKeyboard()

# Add macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add rotary encoder extension
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define pins for rotary encoder
encoder_handler.pins = [board.GP17, board.GP15, board.GP14]

# Define pins for keyboard
PINS = [board.D3, board.D4, board.D2, board.D1]

# No key matrix
keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed=False,
)

# Set keyboard keymap
keyboard.keymap = [
    [KC.Macro(Press(KC.RSHIFT), Tap(KC.I), Release(KC.RSHIFT)),
     KC.Macro(Press(KC.RSHIFT), Tap(KC.O), Release(KC.RSHIFT)),
     KC.Macro(Press(KC.RCTRL), Tap(KC.S), Release(KC.RCTRL)),
     KC.Macro(Press(KC.RCTRL), Press(KC.RSHIFT), Tap(KC.X), Release(KC.RSHIFT), Release(KC.RCTRL))]
]

# Set rotary encoder map
encoder_handler.map = [
    [KC.LEFT, KC.RIGHT, KC.K]
]

# Start!
if __name__ == '__main__':
    keyboard.go()
