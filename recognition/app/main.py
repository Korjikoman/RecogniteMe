from transcriber import Transcriber


def main():

    audio_file = "test-data\\test.mp3"

    transcriber = Transcriber(
        audio_path=audio_file,
        model_size="small",
        chunks_dir="chunks",
        chunk_duration=20,
        language="en"
    )

    result = transcriber.transcribe_big_audio()

    print("\nFINAL RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()