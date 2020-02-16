import os
import re

from itertools import zip_longest

from tinkoff_voicekit_client import ClientTTS as _ClientTTS
from tinkoff_voicekit_client.TTS.helper_tts import (
    get_encoder,
    save_synthesize_wav
)


class ClientTTS(_ClientTTS):
    _DEFAULT_CONFIG = {
        "audio_encoding": "LINEAR16",
        "sample_rate_hertz": 48000
    }

    _TIME_SECTION_PATTERN = r"#\([1-9]\d*\)"

    def __init__(self, API_KEY, SECRET_KEY):
        super().__init__(API_KEY, SECRET_KEY)
        self.get_chunk = get_encoder(
            ClientTTS._DEFAULT_CONFIG["audio_encoding"],
            ClientTTS._DEFAULT_CONFIG["sample_rate_hertz"]
        )

    def synthesize_with_pause(self, text: str, file_name: str, output_dir=os.curdir):
        os.makedirs(output_dir, exist_ok=True)
        silence_chunks = ClientTTS._get_silence_chunks(text)
        splited_text = ClientTTS._split_text_by_time_sections(text)

        audio_chunks = []
        for part_text, silence_chunk in zip_longest(splited_text, silence_chunks):
            audio_chunks += self._handle_responses(part_text, silence_chunk)

        save_synthesize_wav(
            bytes(audio_chunks),
            os.path.join(output_dir, file_name),
            ClientTTS._DEFAULT_CONFIG["sample_rate_hertz"]
        )

    def _handle_responses(self, part_text, silence_chunk):
        audio_chunks = []
        if part_text and part_text.strip() != "3":
            synthesis_responses = self.streaming_synthesize(part_text, ClientTTS._DEFAULT_CONFIG)
            audio_chunks += self._get_audio_chunks(synthesis_responses)
        if silence_chunk:
            audio_chunks += silence_chunk
        return audio_chunks

    def _get_audio_chunks(self, rows_responses):
        audio_chunks = []
        for row_response in rows_responses:
            for response in row_response:
                audio_chunks += self.get_chunk(response.audio_chunk)
        return audio_chunks

    @staticmethod
    def _get_silence_chunks(text: str):
        silence_chunks = []
        one_quant_of_silence = 2 * 4800
        for silence_length in ClientTTS._get_silence_lengths(text):
            silence_chunks.append([0]*(silence_length * one_quant_of_silence))
        return silence_chunks

    @staticmethod
    def _get_silence_lengths(text):
        time_sections = re.findall(ClientTTS._TIME_SECTION_PATTERN, text)
        time_section_values = map(lambda section: int(section[2:-1]), time_sections)
        return list(time_section_values)

    @staticmethod
    def _split_text_by_time_sections(text):
        return re.split(ClientTTS._TIME_SECTION_PATTERN, text)
