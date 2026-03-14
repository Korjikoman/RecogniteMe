import pika
import json
from recognizer import Recognizer


class QueueReader:

    def __init__(self, host="localhost", queue_name="speech_jobs"):

        self.host = host
        self.queue_name = queue_name
        self.recognizer = Recognizer()

    def start(self):

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )

        channel = connection.channel()

        channel.queue_declare(queue=self.queue_name)

        print("[QUEUE] Waiting for messages...")

        channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback
        )

        channel.start_consuming()

    def callback(self, ch, method, properties, body):

        data = json.loads(body)

        audio_path = data["audio"]

        print("[QUEUE] Processing:", audio_path)

        text = self.recognizer.transcribe(audio_path)

        result = {
            "text": text
        }

        print("[QUEUE] Result:", result)

        ch.basic_ack(delivery_tag=method.delivery_tag)