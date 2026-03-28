import requests
import os



class DataController:
    def __init__(self, data, url):
        self.data = data
        self.url = url

    def send_data(self):
        try:
            response = requests.post(self.url, self.data)
            response.raise_for_status()
            print(f"Data sent successfully: {response.text}")
            return response

        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e} ")
            return None