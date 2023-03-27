import tkinter as tk
from tkinter import ttk
from mediachest.gui.tabs.base_tab import BaseTab
from mediachest.core.hardware_manager import HardwareManager

class FMRadioTab(BaseTab):
    """
    The FMRadioTab class represents the FM Radio tab in the main window.
    It inherits from the BaseTab class and provides FM Radio-specific functionality (Req. 15, 17).
    """

    def __init__(self, parent, hardware_manager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Store the microkernel for executing the FM Radio plugin
        self.hardware_manager = hardware_manager

        # Add FM Radio-specific widgets and functionality (Req. 17)
        self.create_fm_radio_widgets()

    def create_fm_radio_widgets(self):
        """
        Create FM Radio-specific widgets (Req. 17).
        """
        # Example: Add a "Frequency" label and entry to the FM Radio tab (Req. 19)
        self.frequency_label = ttk.Label(self, text="Frequency (MHz):")
        self.frequency_label.grid(row=0, column=0, padx=5, pady=5)

        self.frequency_entry = ttk.Entry(self)
        self.frequency_entry.grid(row=0, column=1, padx=5, pady=5)

    def setup_rotary_encoder(self):
        """
        Set up the rotary encoder for listening to frequency change events.
        """
        self.hardware_manager.setup_rotary_encoder(self.on_rotary_change)

    def on_rotary_change(self, direction):
        try:
            current_frequency = float(self.frequency_entry.get())
            updated_frequency = current_frequency + direction * 0.1
            self.frequency_entry.delete(0, tk.END)
            self.frequency_entry.insert(0, "{:.1f}".format(updated_frequency))
        except ValueError:
            pass
