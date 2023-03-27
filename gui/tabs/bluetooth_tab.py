import tkinter as tk
from tkinter import ttk
from mediachest.gui.tabs.base_tab import BaseTab

class BluetoothTab(BaseTab):
    """
    The BluetoothTab class represents the Bluetooth tab in the main window.
    It inherits from the BaseTab class and provides Bluetooth-specific functionality (Req. 15, 16).
    """

    def __init__(self, parent, microkernel, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Store the microkernel for executing the Bluetooth plugin
        self.microkernel = microkernel

        # Add Bluetooth-specific widgets and functionality (Req. 16)
        self.create_bluetooth_widgets()

    def create_bluetooth_widgets(self):
        """
        Create Bluetooth-specific widgets (Req. 16).
        """
        # Example: Add a "Connect" button to the Bluetooth tab (Req. 18)
        self.connect_button = ttk.Button(self, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=2, padx=5, pady=5)

    def play(self):
        """
        Overrides the play method from BaseTab to provide the actual play functionality for Bluetooth (Req. 23).
        """
        # Execute the play functionality of the Bluetooth plugin
        self.microkernel.execute_plugin("bluetooth_plugin", "play")

    def stop(self):
        """
        Overrides the stop method from BaseTab to provide the actual stop functionality for Bluetooth (Req. 24).
        """
        # Execute the stop functionality of the Bluetooth plugin
        self.microkernel.execute_plugin("bluetooth_plugin", "stop")

    def connect(self):
        """
        Connect button callback to establish a Bluetooth connection (Req. 18).
        """
        # Execute the connect functionality of the Bluetooth plugin
        self.microkernel.execute_plugin("bluetooth_plugin", "connect")
