# mediachest/plugins/local_media/local_media_plugin.py
# Implements the Local Media functionality (Requirement 6)

# Import necessary libraries and modules
from mediachest.core.microkernel import Microkernel
import vlc

class LocalMediaPlugin:
    def __init__(self):
        # Initialize the Local Media plugin
        self.media_path = None
        self.player = vlc.Instance().media_player_new()

    def execute(self, command, *args, **kwargs):
        """
        Executes the Local Media plugin functionality.

        :param command: The command to execute (str)
        :param args: The positional arguments to pass to the plugin
        :param kwargs: The keyword arguments to pass to the plugin
        """
        if command == "set_media_path":
            return self.set_media_path(*args)
        elif command == "play":
            return self.play_media()
        elif command == "stop":
            return self.stop_media()
        else:
            raise ValueError(f"Unknown command '{command}' for LocalMediaPlugin.")

    def set_media_path(self, media_path):
        """
        Sets the local media file path (Requirement 6).

        :param media_path: The local media file path to set
        :return: A message indicating the new media path
        """
        self.media_path = media_path
        return f"Local Media path set to {self.media_path}"

    def play_media(self):
        """
        Starts playing the local media file (Requirement 6).

        :return: A message indicating the local media is playing
        """
        if self.media_path is None:
            return "Please set the local media file path before playing"

        media = self.player.get_instance().media_new(self.media_path)
        self.player.set_media(media)
        self.player.play()

        return f"Playing Local Media from {self.media_path}"

    def stop_media(self):
        """
        Stops playing the local media file (Requirement 6).

        :return: A message indicating the local media is stopped
        """
        self.player.stop()
        return "Local Media stopped"
