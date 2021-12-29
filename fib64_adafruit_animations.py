# Animations for the Fibonacci 64 Micro from Evil Genius Labs
import board
import neopixel
import time
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimationSequence

from adafruit_led_animation.color import (
    AMBER, #(255, 100, 0)
    AQUA, # (50, 255, 255)
    BLACK, #OFF (0, 0, 0)
    BLUE, # (0, 0, 255)
    CYAN, # (0, 255, 255)
    GOLD, # (255, 222, 30)
    GREEN, # (0, 255, 0)
    JADE, # (0, 255, 40)
    MAGENTA, #(255, 0, 20)
    OLD_LACE, # (253, 245, 230)
    ORANGE, # (255, 40, 0)
    PINK, # (242, 90, 255)
    PURPLE, # (180, 0, 255)
    RED, # (255, 0, 0)
    TEAL, # (0, 255, 120)
    WHITE, # (255, 255, 255)
    YELLOW, # (255, 150, 0)
    RAINBOW # a list of colors to cycle through
    # RAINBOW is RED, ORANGE, YELLOW, GREEN, BLUE, and PURPLE ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255))
)

INDIGO = (63, 0, 255)
VIOLET = (127, 0, 255)

colors = [RED, MAGENTA, ORANGE, YELLOW, GREEN, JADE, BLUE, INDIGO, VIOLET, PURPLE, BLACK]

pixels_pin = board.MOSI
pixels_num_of_lights = 64
pixel_brightness = 0.2
pixels = neopixel.NeoPixel(pixels_pin, pixels_num_of_lights, brightness = pixel_brightness, auto_write=True)

blink = Blink(pixels, speed=0.5, color=AMBER)

colorcycle = ColorCycle(pixels, 0.1, colors=colors)

chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)

comet = Comet(pixels, speed=0.1, color=RED, tail_length=int(pixels_num_of_lights/4), bounce=True)

pulse = Pulse(pixels, speed=0.05, color=AMBER, period=2)

sparkle = Sparkle(pixels, speed=0.05, color=PURPLE)

sparkle_pulse = SparklePulse(pixels, speed=0.05, period=5, color=BLUE)

rainbow = Rainbow(pixels, speed=0.05, period=2)

rainbow_chase = RainbowChase(pixels, speed=0.01, size=5, spacing=0, step=8)

animations = AnimationSequence(
    blink, colorcycle, chase, comet, pulse, sparkle, sparkle_pulse, rainbow, rainbow_chase, advance_interval=5, auto_clear=True
)

while True:
    #blink.animate()
    #blink_strip.animate()
    #colorcycle.animate()
    #colorcycle_strip.animate()
    #chase.animate()
    #chase_strip.animate()
    #comet.animate()
    #comet_strip.animate()
    #pulse.animate()
    #pulse_strip.animate()
    #sparkle.animate()
    #sparkle_strip.animate()
    #sparkle_pulse.animate()
    #sparkle_pulse_strip.animate()
    #rainbow.animate()
    #rainbow_strip.animate()
    #rainbow_chase.animate()
    #rainbow_chase_strip.animate()
    animations.animate()
