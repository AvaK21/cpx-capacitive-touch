from adafruit_circuitplayground import cp
import time
import board
import touchio

RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (255, 0, 203)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_A7 = touchio.TouchIn(board.A7)
cp.pixels.brightness = 0.05
while True:
    if touch_A3.value:
        cp.pixels.fill(RED)
    elif touch_A4.value:
        cp.pixels.fill(ORANGE)
    elif touch_A5.value:
        cp.pixels.fill(YELLOW)
    elif touch_A6.value:
        cp.pixels.fill(GREEN)
    elif touch_A7.value:
        cp.pixels.fill(BLUE)
    elif touch_A1.value:
        cp.pixels.fill(PURPLE)
    elif touch_A2.value:
        cp.pixels.fill(PINK)
    else:
        cp.pixels.fill((0, 0, 0))
    time.sleep(0.1)