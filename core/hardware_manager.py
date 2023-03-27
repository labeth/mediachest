import RPi.GPIO as GPIO
import threading
import time
import board
import busio
import digitalio

class HardwareManager:
    def __init__(self, config_manager, on_volume_change=None):
        # Store the ConfigManager instance
        self.config_manager = config_manager

        # Initialize the rotary encoder attributes
        self.rotary_encoder_pins = None
        self.rotary_callback = None
        
        # volume NOT DONE
        self.on_volume_change = on_volume_change

        # Set up the rotary encoder
        rotary_left_encoder_gpio = self.config_manager.config_data["hardware"]["left_rotary_encoder_gpio"]
        rotary_right_encoder_gpio = self.config_manager.config_data["hardware"]["right_rotary_encoder_gpio"]
        self.setup_rotary_encoder(rotary_left_encoder_gpio, self.on_left_rotary_encoder_change)
        self.setup_rotary_encoder(rotary_right_encoder_gpio, self.on_right_rotary_encoder_change)

    def setup_rotary_encoder(self, pins, callback):
        """
        Set up the rotary encoder for listening to frequency change events.

        :param pins: A tuple containing the two GPIO pins connected to the rotary encoder
        :param callback: A function to call when the rotary encoder is turned
        """
        # Store the pins and callback
        self.rotary_encoder_pins = pins
        self.rotary_callback = callback

        # Set up the GPIO pins for the rotary encoder
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.rotary_encoder_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Store the initial state of the first rotary encoder pin
        self.last_rotary_state = GPIO.input(self.rotary_encoder_pins[0])

        # Detect events on the first rotary encoder pin and call the rotary_event method
        GPIO.add_event_detect(self.rotary_encoder_pins[0], GPIO.BOTH, callback=self.rotary_event)

    def rotary_event(self, channel):
        """
        Handle a rotary encoder event by calling the stored callback with the direction.

        :param channel: The GPIO channel that triggered the event (unused)
        """
        # Read the current state of the first rotary encoder pin
        current_state = GPIO.input(self.rotary_encoder_pins[0])

        # If the state has changed, determine the direction and call the callback
        if current_state != self.last_rotary_state:
            if GPIO.input(self.rotary_encoder_pins[1]) != current_state:
                self.rotary_callback(1)
            else:
                self.rotary_callback(-1)

        # Update the stored state of the first rotary encoder pin
        self.last_rotary_state = current_state

    def on_left_rotary_encoder_change(self, direction):
        """
        Handle a rotary encoder direction change.

        :param direction: The direction of the rotary encoder change (1 or -1)
        """
        # Implement your logic for handling rotary encoder changes (e.g., changing the FM radio frequency)
        pass
       
    def on_right_rotary_encoder_change(self, direction):
        """
        Handle a rotary encoder direction change.

        :param direction: The direction of the rotary encoder change (1 or -1)
        """
        # Implement your logic for handling rotary encoder changes (e.g., changing the FM radio frequency)
        pass