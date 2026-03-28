from audioSlicer import AudioSlicer
from recognizer import Recognizer
import json
import os
class Transcriber:

    def __init__(self, audio_path, model_size, chunks_dir, chunk_duration, language, path_to_save_json):

        self.audio_path = audio_path
        self.model_size = model_size
        self.chunks_dir = chunks_dir
        self.chunk_duration = chunk_duration
        self.language = language
        self.path_to_save_json = path_to_save_json

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
            if os.path.exists(chunk):
                print(f"Удаление -- {chunk}")
                os.remove(chunk)

        


        full_text = full_text.strip()

        json_dump = {"text" : full_text}

        full_text_json = json.dumps(json_dump)

        return full_text_json
    


    def save_text_json(self, text):
        json_dump = {"text" : text}

        os.makedirs(os.path.dirname(self.path_to_save_json), exist_ok=True)
        path = self.path_to_save_json + "/textFromAudio.json"


        with open(path, 'w+', encoding='utf-8') as f:
            json.dump(json_dump, fp=f, indent=2, ensure_ascii=False)
            print(f"Текст успешно сохранен в файл {path} ")
        