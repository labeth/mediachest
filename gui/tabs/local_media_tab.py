import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from mediachest.gui.tabs.base_tab import BaseTab
from mediachest.plugins.local_media import LocalMediaPlugin

class LocalMediaTab(BaseTab):
    def __init__(self, parent):
        BaseTab.__init__(self, parent)
        self.parent = parent

        # Initialize the LocalMediaPlugin for playback (Req. 9)
        self.local_media_plugin = LocalMediaPlugin()

        self.create_widgets()

    def create_widgets(self):
        # Create the file selection button (Design: Dark theme interface)
        self.select_file_button = ttk.Button(self, text="Select File", command=self.select_file)
        self.select_file_button.grid(column=0, row=0, padx=10, pady=10)

        # Create the selected file label (Design: Dark theme interface)
        self.selected_file_label = ttk.Label(self, text="No file selected")
        self.selected_file_label.grid(column=1, row=0, padx=10, pady=10)

        # Create the play button for starting playback of the selected file (Req. 9, 35)
        self.play_button = ttk.Button(self, text="Play", command=self.play_media, state="disabled")
        self.play_button.grid(column=0, row=1, padx=10, pady=10)

    def select_file(self):
        """
        Opens a file dialog to select a local media file for playback (Req. 9).
        """
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav;*.ogg")])
        if file_path:
            self.selected_file_label.config(text=file_path)
            self.play_button.config(state="normal")

    def play_media(self):
        """
        Starts playback of the selected local media file using the LocalMediaPlugin (Req. 9).
        """
        file_path = self.selected_file_label.cget("text")
        if file_path:
            self.local_media_plugin.play(file_path)
