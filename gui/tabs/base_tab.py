import tkinter as tk
from tkinter import ttk

class BaseTab(ttk.Frame):
    """
    BaseTab is the base class for all plugin tabs in the main window.
    It provides a common structure and functionality for each plugin tab (Req. 15).
    """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Create a common layout for all plugin tabs (Req. 15)
        self.create_widgets()

    def create_widgets(self):
        """
        Create widgets common to all plugin tabs (Req. 15).
        This method can be overridden by derived classes to add more widgets specific to each plugin.
        """

        # Example: Add a play and stop button common to all plugin tabs (Req. 23, 24)
        self.play_button = ttk.Button(self, text="Play", command=self.play)
        self.stop_button = ttk.Button(self, text="Stop", command=self.stop)

        self.play_button.grid(row=0, column=0, padx=5, pady=5)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)

    def play(self):
        """
        Play button callback (Req. 23).
        This method should be overridden by derived classes to provide the actual play functionality.
        """
        raise NotImplementedError("Play functionality must be implemented in derived classes.")

    def stop(self):
        """
        Stop button callback (Req. 24).
        This method should be overridden by derived classes to provide the actual stop functionality.
        """
        raise NotImplementedError("Stop functionality must be implemented in derived classes.")
