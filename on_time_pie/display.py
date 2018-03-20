import time
from threading import Thread
import RPi.GPIO as GPIO

DISPLAY_NUMBERS = {
    '0': (1, 1, 1, 1, 1, 1, 0),
    '1': (0, 1, 1, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1),
    '3': (1, 1, 1, 1, 0, 0, 1),
    '4': (0, 1, 1, 0, 0, 1, 1),
    '5': (1, 0, 1, 1, 0, 1, 1),
    '6': (1, 0, 1, 1, 1, 1, 1),
    '7': (1, 1, 1, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1)
}


class Display(Thread):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.segment_pins = (11, 4, 23, 8, 7, 10, 18)
        self.digit_pins = (22, 27, 17, 24)
        self.point_pin = 25
        self.numbers = "0000"
        for segment_pin in self.segment_pins:
            GPIO.setup(segment_pin, GPIO.OUT)
            GPIO.output(segment_pin, 0)
        for digit_pin in self.digit_pins:
            GPIO.setup(digit_pin, GPIO.OUT)
            GPIO.output(digit_pin, 1)
        GPIO.setup(self.point_pin, 0)
        Thread.__init__(self)

    def display(self):
        for digit_position, digit_pin in enumerate(self.digit_pins):
            for segment_position, segment_pin in enumerate(self.segment_pins):
                GPIO.output(segment_pin, DISPLAY_NUMBERS[self.numbers[
                    digit_position]][segment_position])
            if digit_position == 1:  # display the . between line and minutes
                GPIO.output(self.point_pin, 1)
            else:
                GPIO.output(self.point_pin, 0)
            GPIO.output(digit_pin, 0)
            time.sleep(0.001)
            GPIO.output(digit_pin, 1)

    def run(self):
        try:
            while True:
                self.display()
        finally:
            GPIO.cleanup()
