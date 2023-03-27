# mediachest/plugins/internet_radio/internet_radio_plugin.py
# Implements the Internet Radio functionality (Requirement 7)

# Import necessary libraries and modules
from mediachest.core.microkernel import Microkernel
import vlc

class InternetRadioPlugin:
    def __init__(self):
        # Initialize the Internet Radio plugin
        self.url = None
        self.player = vlc.Instance().media_player_new()

    def execute(self, command, *args, **kwargs):
        """
        Executes the Internet Radio plugin functionality.

        :param command: The command to execute (str)
        :param args: The positional arguments to pass to the plugin
        :param kwargs: The keyword arguments to pass to the plugin
        """
        if command == "set_url":
            return self.set_url(*args)
        elif command == "play":
            return self.play_radio()
        elif command == "stop":
            return self.stop_radio()
        else:
            raise ValueError(f"Unknown command '{command}' for InternetRadioPlugin.")

    def set_url(self, url):
        """
        Sets the internet radio URL (Requirement 7).

        :param url: The internet radio URL to set
        :return: A message indicating the new URL
        """
        self.url = url
        return f"Internet Radio URL set to {self.url}"

    def play_radio(self):
        """
        Starts playing the internet radio (Requirement 7).

        :return: A message indicating the internet radio is playing
        """
        if self.url is None:
            return "Please set the internet radio URL before playing"

        media = self.player.get_instance().media_new(self.url)
        self.player.set_media(media)
        self.player.play()

        return f"Playing Internet Radio from {self.url}"

    def stop_radio(self):
        """
        Stops playing the internet radio (Requirement 7).

        :return: A message indicating the internet radio is stopped
        """
        self.player.stop()
        return "Internet Radio stopped"
