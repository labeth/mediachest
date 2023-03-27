import tkinter as tk
from tkinter import ttk
from mediachest.gui.tabs.base_tab import BaseTab
from mediachest.plugins.internet_radio import InternetRadioPlugin
from mediachest.config.config_manager import ConfigManager

class InternetRadioTab(BaseTab):
    def __init__(self, parent):
        BaseTab.__init__(self, parent)
        self.parent = parent

        # Load the internet radio stations from the configuration (Req. 12)
        self.config_manager = ConfigManager()
        self.radio_stations = self.config_manager.get_internet_radio_stations()

        # Initialize the InternetRadioPlugin for playback (Req. 12)
        self.radio_plugin = InternetRadioPlugin()

        self.create_widgets()
        self.update_station_list()

    def create_widgets(self):
        # Create the station list label (Design: Dark theme interface)
        self.station_listbox_label = ttk.Label(self, text="Station List:")
        self.station_listbox_label.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        # Create the station listbox for displaying the available stations (Req. 12)
        self.station_listbox = tk.Listbox(self, height=10, width=50)
        self.station_listbox.grid(column=0, row=1, padx=10, pady=10)

        # Create the play button for starting playback of the selected station (Req. 12, 35)
        self.play_button = ttk.Button(self, text="Play", command=self.play_station)
        self.play_button.grid(column=1, row=1, padx=10, pady=10)

    def update_station_list(self):
        """
        Updates the station listbox with the available internet radio stations (Req. 12).
        """
        self.station_listbox.delete(0, tk.END)
        for station in self.radio_stations:
            self.station_listbox.insert(tk.END, f"{station['name']} ({station['url']})")

    def play_station(self):
        """
        Starts playback of the selected internet radio station using the InternetRadioPlugin (Req. 12).
        """
        selected_station_index = self.station_listbox.curselection()
        if selected_station_index:
            station = self.radio_stations[selected_station_index[0]]
            self.radio_plugin.play(station['url'])
