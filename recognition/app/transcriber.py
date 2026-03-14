from audioSlicer import AudioSlicer
from recognizer import Recognizer


class Transcriber:

    def __init__(self, audio_path, model_size, chunks_dir, chunk_duration, language):

        self.audio_path = audio_path
        self.model_size = model_size
        self.chunks_dir = chunks_dir
        self.chunk_duration = chunk_duration
        self.language = language

        self.recognizer = Recognizer(model_size, language)

    def transcribe_big_audio(self):

        slicer = AudioSlicer(
            self.audio_path,
            self.chunk_duration,
            self.chunks_dir
        )

        chunks = slicer.sliceIntoChunks()

        full_text = ""

        for chunk in chunks:

            text = self.recognizer.transcribe(chunk)

            full_text += text + " "

        full_text = full_text.strip()

        return full_text