# mediachest/core/audio_processing.py
# Handles audio playback using PyDub (Requirement 30, 31, 32) and audio conversion for compatibility with the equalizer and output functions (Requirement 33)

from pydub import AudioSegment
from pydub.playback import play as pydub_play

class AudioProcessing:
    """
    The AudioProcessing class is responsible for handling audio playback and conversion using PyDub.
    It implements the requirements for audio playback (Req. 30, 31, 32) and audio conversion (Req. 33).
    """

    def __init__(self):
        pass

    def play_audio(self, audio_data):
        """
        Play the audio data using PyDub playback functionality (Req. 30).

        :param audio_data: The audio data to play, in a format supported by PyDub
        """
        # Create an AudioSegment from the audio data and play it (Req. 31)
        audio_segment = AudioSegment.from_file(audio_data)
        pydub_play(audio_segment)

    def convert_audio(self, audio_data, target_format):
        """
        Convert the audio data to the specified target format for compatibility with the equalizer and output functions (Req. 33).

        :param audio_data: The audio data to convert, in a format supported by PyDub
        :param target_format: The target format of the audio data, such as 'wav' or 'mp3'
        :return: The converted audio data
        """
        # Create an AudioSegment from the audio data and export it in the target format (Req. 32)
        audio_segment = AudioSegment.from_file(audio_data)
        converted_audio_data = audio_segment.export(format=target_format)

        return converted_audio_data