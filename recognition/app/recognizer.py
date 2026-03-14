from faster_whisper import WhisperModel


class Recognizer:

    def __init__(self, model_size="small", language="en"):
        self.language = language
        print("[RECOGNIZER] Loading model...")
        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )
        print("[RECOGNIZER] Model loaded")

    def transcribe(self, audio_path):

        segments, info = self.model.transcribe(
            audio_path,
            language=self.language
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        text = text.strip()

        print(f"[RECOGNIZER] TEXT == {text}")

        return text