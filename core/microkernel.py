# mediachest/core/microkernel.py
# Implements the Microkernel Architecture Pattern (Requirement 14)

# Import necessary libraries and modules
import importlib
import os

class Microkernel:
    def __init__(self):
        # Initializes the plugin registry
        self.plugin_registry = {}

    def register_plugin(self, plugin_name, plugin_class):
        """
        Registers a plugin in the microkernel.

        :param plugin_name: The name of the plugin (str)
        :param plugin_class: The plugin class to be registered
        """
        # Adds the plugin to the plugin registry
        self.plugin_registry[plugin_name] = plugin_class

    def load_plugins(self, plugin_directory):
        """
        Loads all the plugins from a specified directory.

        :param plugin_directory: The directory containing the plugins (str)
        """
        # Iterates through the files in the plugin directory
        for filename in os.listdir(plugin_directory):
            # Skips the file if it's not a Python file
            if not filename.endswith(".py"):
                continue

            # Imports the plugin module
            module_name = os.path.splitext(filename)[0]
            module = importlib.import_module(f"mediachest.plugins.{module_name}.{module_name}")

            # Registers the plugin if it has a register_plugin function
            if hasattr(module, "register_plugin"):
                module.register_plugin(self)

    def execute_plugin(self, plugin_name, *args, **kwargs):
        """
        Executes a plugin with the specified name.

        :param plugin_name: The name of the plugin to execute (str)
        :param args: The positional arguments to pass to the plugin
        :param kwargs: The keyword arguments to pass to the plugin
        :return: The result of the plugin execution
        """
        # Retrieves the plugin class from the registry
        plugin_class = self.plugin_registry.get(plugin_name)

        # Raises an error if the plugin is not found
        if plugin_class is None:
            raise ValueError(f"Plugin {plugin_name} not found in the registry.")

        # Instantiates the plugin and executes it
        plugin_instance = plugin_class()
        return plugin_instance.execute(*args, **kwargs)
