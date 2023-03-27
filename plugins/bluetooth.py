# mediachest/plugins/bluetooth/bluetooth_plugin.py
# Implements the Bluetooth functionality (Requirement 8)

# Import necessary libraries and modules
from mediachest.core.microkernel import Microkernel
import bluetooth
import threading
from pydbus import SystemBus
from gi.repository import GLib

class BluetoothPlugin:
    def __init__(self):
        # Initialize the Bluetooth plugin
        self.discovered_devices = []
        self.is_scanning = False

    def execute(self, command, *args, **kwargs):
        """
        Executes the Bluetooth plugin functionality.

        :param command: The command to execute (str)
        :param args: The positional arguments to pass to the plugin
        :param kwargs: The keyword arguments to pass to the plugin
        """
        if command == "scan":
            return self.scan_devices()
        elif command == "connect":
            return self.connect_device(*args)
        else:
            raise ValueError(f"Unknown command '{command}' for BluetoothPlugin.")

    def scan_devices(self):
        """
        Scans for nearby Bluetooth devices and updates the list of discovered devices (Requirement 8).

        :return: List of discovered Bluetooth devices
        """
        if not self.is_scanning:
            self.is_scanning = True
            self.discovered_devices = []
            devices = bluetooth.discover_devices(lookup_names=True)

            for addr, name in devices:
                self.discovered_devices.append({"address": addr, "name": name})

            self.is_scanning = False

        return self.discovered_devices

    def connect_device(self, address):
        """
        Connects to a Bluetooth device with the specified address (Requirement 8).

        :param address: The Bluetooth address of the device to connect
        :return: A message indicating the connection status
        """
        try:
            bus = SystemBus()
            adapter = bus.get('org.bluez', '/org/bluez/hci0')
            adapter.StartDiscovery()

            device = None
            mng_objs = bus.get('org.bluez', '/')
            for path, interfaces in mng_objs.GetManagedObjects().items():
                if 'org.bluez.Device1' in interfaces:
                    dev = bus.get('org.bluez', path)
                    if dev.Address == address:
                        device = dev
                        break

            if device is None:
                raise Exception("Device not found")

            device.Connect()
            adapter.StopDiscovery()

            return f"Connected to Bluetooth device at address {address}"
        except Exception as e:
            return f"Error connecting to Bluetooth device: {str(e)}"

# Register the BluetoothPlugin with the Microkernel (Requirement 19)
def register_plugin(microkernel: Microkernel):
    microkernel.register_plugin("bluetooth", BluetoothPlugin)