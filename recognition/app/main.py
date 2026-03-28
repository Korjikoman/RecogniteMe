from transcriber import Transcriber
from dataController import DataController


def main():

    audio_file = "recognition/test-data/test.mp3"
    path_to_save_json = "recognition/json"
    backend_url = "127.0.0.1/api/data-from-python-service"

    transcriber = Transcriber(
        audio_path=audio_file,
        model_size="small",
        chunks_dir="chunks",
        chunk_duration=20,
        language="en",
        path_to_save_json=path_to_save_json
    )

    data = transcriber.transcribe_big_audio()



    print("\nFINAL RESULT:\n")
    print(data)

    data_controller = DataController(data, backend_url)
    data_controller.send_data()



if __name__ == "__main__":
    main()