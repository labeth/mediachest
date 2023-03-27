import tkinter as tk
from tkinter import ttk
from mediachest.core.microkernel import Microkernel
from mediachest.core.hardware_manager import HardwareManager
from mediachest.config.config_manager import ConfigManager

from mediachest.gui.tabs.bluetooth_tab import BluetoothTab
from mediachest.gui.tabs.fm_radio_tab import FMRadioTab
from mediachest.gui.tabs.internet_radio_tab import InternetRadioTab
from mediachest.gui.tabs.local_media_tab import LocalMediaTab
from mediachest.gui.tabs.spotify_tab import SpotifyTab

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.microkernel = Microkernel()
        self.config_manger = ConfigManager()
        self.hardware_manager = HardwareManager(self.config_manger)
        # Set up the main window (Req. 15, 16, 17, 18, 19)
        self.title("Music Center")
        self.geometry("800x600")

        # Create the tabbed interface (Req. 15)
        self.tab_control = ttk.Notebook(self)

        # Add the tabs for each plugin (Req. 15, 16, 17, 18, 19)
        self.bluetooth_tab = BluetoothTab(self.tab_control, self.microkernel)
        self.fm_radio_tab = FMRadioTab(self.tab_control, self.hardware_manager)
        self.internet_radio_tab = InternetRadioTab(self.tab_control)
        self.local_media_tab = LocalMediaTab(self.tab_control)
        self.spotify_tab = SpotifyTab(self.tab_control, self.config_manger)

        self.tab_control.add(self.bluetooth_tab, text="Bluetooth")
        self.tab_control.add(self.fm_radio_tab, text="FM Radio")
        self.tab_control.add(self.internet_radio_tab, text="Internet Radio")
        self.tab_control.add(self.local_media_tab, text="Local Media")
        self.tab_control.add(self.spotify_tab, text="Spotify")

        # Display the tab control (Req. 15)
        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    # Initialize and run the main application loop (Req. 15)
    app = MainWindow()
    app.mainloop()
