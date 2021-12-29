# A simple rainbow animation for the Fibonacci 64 Micro by Evil Genius Labs
# Video demo can be found by searching: https://YouTube.com/profgallaugher
import board, time, neopixel, digitalio, touchio
from rainbowio import colorwheel

num_of_leds = 64
led_pin = board.MOSI
led_brightness = 0.2
leds = neopixel.NeoPixel(led_pin, num_of_leds, brightness=led_brightness, auto_write=False)
leds.fill((0, 0, 255))

while True:
    for i in range(num_of_leds):
        leds[i] = colorwheel(i*4)
        leds.write()
        time.sleep(0.01)
    for i in range (led_brightness*100, -1, -1):
        leds.brightness = i/100
        leds.write()
        time.sleep(0.01)
    leds.brightness = led_brightness
    leds.fill((0, 0, 0))
    leds.write()



