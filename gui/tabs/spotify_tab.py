import tkinter as tk
from tkinter import ttk
from mediachest.gui.tabs.base_tab import BaseTab
from mediachest.plugins.spotify import SpotifyPlugin

class SpotifyTab(BaseTab):
    def __init__(self, parent, config_manager):
        BaseTab.__init__(self, parent)
        self.parent = parent

        # Initialize the SpotifyPlugin for playback (Req. 7)
        self.spotify_plugin = SpotifyPlugin(config_manager)

        self.create_widgets()

    def create_widgets(self):
        # Create a label for the search entry (Design: Dark theme interface)
        self.search_label = ttk.Label(self, text="Search for a track:")
        self.search_label.grid(column=0, row=0, padx=10, pady=10)

        # Create the search entry (Design: Dark theme interface)
        self.search_entry = ttk.Entry(self)
        self.search_entry.grid(column=1, row=0, padx=10, pady=10)

        # Create the search button for initiating the search (Req. 7)
        self.search_button = ttk.Button(self, text="Search", command=self.search_track)
        self.search_button.grid(column=2, row=0, padx=10, pady=10)

        # Create the play button for starting playback of the selected track (Req. 7, 35)
        self.play_button = ttk.Button(self, text="Play", command=self.play_track, state="disabled")
        self.play_button.grid(column=0, row=1, padx=10, pady=10)

        # Create a listbox for displaying search results (Design: Dark theme interface)
        self.track_list = tk.Listbox(self, width=50)
        self.track_list.grid(column=1, row=1, padx=10, pady=10)

    def search_track(self):
        """
        Searches for a track on Spotify using the SpotifyPlugin (Req. 7).
        """
        query = self.search_entry.get()
        if query:
            results = self.spotify_plugin.search_track(query)

            # Clear the listbox before displaying new search results
            self.track_list.delete(0, tk.END)

            # Add search results to the listbox (Req. 7)
            for track in results:
                self.track_list.insert(tk.END, track['name'])

            # Enable the play button when there are search results
            if results:
                self.play_button.config(state="normal")

    def play_track(self):
        """
        Starts playback of the selected track on Spotify using the SpotifyPlugin (Req. 7).
        """
        track_index = self.track_list.curselection()
        if track_index:
            self.spotify_plugin.play_track(track_index[0])
