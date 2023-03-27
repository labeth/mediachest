# mediachestpluginsspotifyspotify_plugin.py
# Implements the Spotify functionality (Requirement 5)

# Import necessary libraries and modules
from mediachest.core.microkernel import Microkernel
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyPlugin:
    def __init__(self, config_manager):
        # Load Spotify settings from the configuration manager
        self.config_manager = config_manager
        self.spotify_settings = self.config_manager.get_spotify_settings()

        # Initialize the Spotify plugin with authentication
        #self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.spotify_settings['client_id'], client_secret=self.spotify_settings['client_secret'], redirect_uri=self.spotify_settings['redirect_uri'], scope=streaming user-read-playback-state))

    def execute(self, command, args, kwargs):
        """
        Executes the Spotify plugin functionality.

        param command The command to execute (str)
        param args The positional arguments to pass to the plugin
        param kwargs The keyword arguments to pass to the plugin
        """
        if command == play:
            return self.play_media(args)
        elif command == pause:
            return self.pause_media()
        elif command == stop:
            return self.stop_media()
        else:
            raise ValueError(f"Unknown command '{command}' for SpotifyPlugin.")

    def play_media(self, track_uri=None):
        """
        Starts playing the specified Spotify track or resumes playback (Requirement 5).

        param track_uri The Spotify track URI (str, optional)
        return A message indicating the Spotify track is playing
        """
        if track_uri:
            self.sp.start_playback(uris=[track_uri])
            return f"Playing Spotify track {track_uri}"
        else:
            self.sp.start_playback()
            return "Resuming Spotify playback"

    def pause_media(self):
        """
        Pauses the current Spotify track playback (Requirement 5).

        return A message indicating the Spotify track is paused
        """
        self.sp.pause_playback()
        return "Spotify playback paused"

    def stop_media(self):
        """
        Stops the current Spotify track playback (Requirement 5).

        return A message indicating the Spotify track is stopped
        """
        self.sp.pause_playback()
        return "Spotify playback stopped"
