import subprocess
import os


class AudioSlicer:

    def __init__(self, path, chunk_duration, save_dir):

        self.path = path
        self.chunk_duration = chunk_duration
        self.save_dir = "recognition/" + save_dir

        os.makedirs(save_dir, exist_ok=True)

    def sliceIntoChunks(self):

        output_pattern = os.path.join(self.save_dir, "chunk_%03d.wav")

        cmd = [
            "ffmpeg",
            "-i", self.path,
            "-f", "segment",
            "-segment_time", str(self.chunk_duration),
            "-c", "copy",
            "-y",
            output_pattern
        ]

        subprocess.run(cmd, check=True)

        chunks = sorted(
            os.path.join(self.save_dir, f)
            for f in os.listdir(self.save_dir)
            if f.endswith(".wav")
        )

        print(f"[SLICER] Created {len(chunks)} chunks")

        return chunks
