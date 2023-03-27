import numpy as np
from scipy.signal import lfilter

class Equalizer:
    """
    The Equalizer class is responsible for adjusting the audio output based on user-configurable settings.
    It implements equalizer functionality (Req. 13, 26, 27, 28, and 29).
    """

    def __init__(self, config_manager):
        # Load equalizer settings from the configuration manager (Req. 29)
        self.config_manager = config_manager
        self.equalizer_settings = self.config_manager.get_equalizer_settings()

    def adjust_audio(self, audio_data, sample_rate):
        """
        Adjust the audio data based on the equalizer settings (Req. 13, 27, 28).

        :param audio_data: NumPy array of audio data
        :param sample_rate: The sample rate of the audio data
        :return: Adjusted audio data as a NumPy array
        """

        # Apply equalizer adjustments to each frequency band (Req. 27)
        for band in self.equalizer_settings['bands']:
            audio_data = self.apply_filter(audio_data, sample_rate, band['frequency'], band['gain'])

        return audio_data

    def apply_filter(self, audio_data, sample_rate, frequency, gain):
        """
        Apply a filter to the audio data for the specified frequency and gain.

        :param audio_data: NumPy array of audio data
        :param sample_rate: The sample rate of the audio data
        :param frequency: The center frequency of the band
        :param gain: The gain to apply to the frequency band
        :return: Filtered audio data as a NumPy array
        """

        # Calculate filter coefficients for the specified frequency and gain
        b, a = self.calculate_coefficients(sample_rate, frequency, gain)

        # Apply the filter to the audio data using the calculated coefficients
        filtered_audio_data = lfilter(b, a, audio_data)

        return filtered_audio_data

    def calculate_coefficients(self, sample_rate, frequency, gain):
        """
        Calculate the filter coefficients for the specified frequency and gain.

        :param sample_rate: The sample rate of the audio data
        :param frequency: The center frequency of the band
        :param gain: The gain to apply to the frequency band
        :return: A tuple (b, a) containing the filter coefficients
        """

        # Use an example filter design method (replace with the desired filter design)
        # Note: This is just a placeholder and should be replaced with a proper filter design
        b = [1]
        a = [1]

        return b, a

    def update_equalizer_settings(self, new_settings):
        """
        Update the equalizer settings and persist them (Req. 28, 29).

        :param new_settings: The new equalizer settings
        """

        self.equalizer_settings = new_settings
        self.config_manager.set_equalizer_settings(new_settings)
