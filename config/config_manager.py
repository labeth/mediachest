# mediachest/config/config_manager.py
import os
import yaml
import jsonschema

class ConfigManager:
    def __init__(self, config_file=None):
        """
        Initializes the ConfigManager.

        :param config_file: The path to the configuration file (str)
        """
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), 'default_config.yaml')

        with open(config_file, 'r') as file:
            self.config_data = yaml.safe_load(file)
        
        self.validate_config()

    def validate_config(self):
        """
        Validate the configuration data according to the JSON schema.
        """
        schema_file = os.path.join(os.path.dirname(__file__), 'schema.json')
        with open(schema_file, 'r') as file:
            schema_data = yaml.safe_load(file)

        try:
            jsonschema.validate(self.config_data, schema_data)
        except jsonschema.ValidationError as e:
            raise ValueError(f"Invalid configuration: {e.message}")

    def get_equalizer_settings(self):
        """
        Get the equalizer settings from the configuration (Req. 29).

        :return: A dictionary containing the equalizer settings
        """
        return self.config_data.get('equalizer', {})

    def set_equalizer_settings(self, new_settings):
        """
        Update the equalizer settings in the configuration and persist them (Req. 29).

        :param new_settings: The new equalizer settings (dict)
        """
        self.config_data['equalizer'] = new_settings
        self.save_config()

    def get_internet_radio_stations(self):
        """
        Get the list of internet radio stations from the configuration.

        :return: A list of internet radio stations
        """
        return self.config_data.get('internet_radio', {}).get('stations', [])

    def get_spotify_settings(self):
        """
        Get the Spotify settings from the configuration.

        :return: A dictionary containing the Spotify settings
        """
        return self.config_data.get('spotify', {})

    def save_config(self):
        """
        Save the configuration data to the configuration file.
        """
        config_file = os.path.join(os.path.dirname(__file__), 'default_config.yaml')
        with open(config_file, 'w') as file:
            yaml.safe_dump(self.config_data, file, default_flow_style=False)

    # Add more methods as needed ...
