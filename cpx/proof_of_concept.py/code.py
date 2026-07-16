from adafruit_circuitplayground import cp
import time
import board
import touchio

RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
PINK = (255, 0, 255)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_A7 = touchio.TouchIn(board.A7)
cp.pixels.brightness = 0.05
# A3_value = touch_A3.raw_value
# A2_value = touch_A2.raw_value
# A1_value = touch_A1.raw_value
# A4_value = touch_A4.raw_value
# A5_value = touch_A5.raw_value
# A6_value = touch_A6.raw_value
# A7_value = touch_A7.raw_value



while True:
    if cp.switch:
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
    # A3_value = touch_A3.raw_value
    # A2_value = touch_A2.raw_value
    # A1_value = touch_A1.raw_value
    # A4_value = touch_A4.raw_value
    # A5_value = touch_A5.raw_value
    # A6_value = touch_A6.raw_value
    # A7_value = touch_A7.raw_value

    #print("A2: ", A2_value, "A3: ", A3_value, "A1: ", A1_value, "A4: ", A4_value, "A5: ", A5_value, "A6: ", A6_value, "A7: ", A7_value)
    time.sleep(0.1)