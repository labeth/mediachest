# mediachest/plugins/fm_radio/fm_radio_plugin.py
# Implements the FM Radio functionality (Requirement 9)

# Import necessary libraries and modules
from mediachest.core.microkernel import Microkernel
from rtlsdr import RtlSdr
from scipy.signal import butter, lfilter
import numpy as np
import pyaudio

class FMRadioPlugin:
    def __init__(self):
        # Initialize the FM Radio plugin
        self.frequency = None
        self.is_playing = False
        self.sdr = RtlSdr()
        self.p = pyaudio.PyAudio()

    def execute(self, command, *args, **kwargs):
        """
        Executes the FM Radio plugin functionality.

        :param command: The command to execute (str)
        :param args: The positional arguments to pass to the plugin
        :param kwargs: The keyword arguments to pass to the plugin
        """
        if command == "set_frequency":
            return self.set_frequency(*args)
        elif command == "play":
            return self.play_radio()
        elif command == "stop":
            return self.stop_radio()
        else:
            raise ValueError(f"Unknown command '{command}' for FMRadioPlugin.")

    def set_frequency(self, frequency):
        """
        Sets the FM Radio frequency (Requirement 9).

        :param frequency: The FM Radio frequency to set
        :return: A message indicating the new frequency
        """
        self.frequency = frequency
        return f"FM Radio frequency set to {self.frequency} MHz"

    def demodulate_fm(self, samples):
        """
        Demodulate FM signal.

        :param samples: The input samples from the SDR
        :return: The demodulated audio samples
        """
        samples = np.array(samples).astype("complex64")
        d = samples[1:] * np.conj(samples[:-1])
        demodulated = np.angle(d)

        return demodulated

    def filter_audio(self, audio_signal, cutoff_freq, sample_rate):
        """
        Filter the audio signal to remove high-frequency noise.

        :param audio_signal: The input audio samples
        :param cutoff_freq: The cutoff frequency for the low-pass filter
        :param sample_rate: The sample rate of the input audio samples
        :return: The filtered audio samples
        """
        nyquist_freq = 0.5 * sample_rate
        normal_cutoff = cutoff_freq / nyquist_freq
        b, a = butter(1, normal_cutoff, btype="low", analog=False)
        filtered_audio = lfilter(b, a, audio_signal)

        return filtered_audio

    def play_radio(self):
        """
        Starts playing the FM Radio (Requirement 9).

        :return: A message indicating the FM Radio is playing
        """
        if self.is_playing:
            return "FM Radio is already playing"

        if self.frequency is None:
            return "Please set the FM Radio frequency before playing"

        self.is_playing = True

        def callback(in_data, frame_count, time_info, status):
            samples = self.sdr.read_samples(256 * 1024)
            demodulated = self.demodulate_fm
