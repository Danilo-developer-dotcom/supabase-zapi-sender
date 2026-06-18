import os
import requests

class Zapi:
    def __init__(self):
        # Carrega as variáveis de ambiente
        self.ZAPI_ID: str = os.getenv("ZAPI_ID")
        self.ZAPI_TOKEN: str = os.getenv("ZAPI_TOKEN")
        self.ZAPI_CLIENT_TOKEN: str = os.getenv("ZAPI_CLIENT_TOKEN")
        # Estabelece conexão com Z-API
        self.url: str = f"https://api.z-api.io/instances/{self.ZAPI_ID}/token/{self.ZAPI_TOKEN}/send-text"
        self.headers: dict = {"Client-Token": self.ZAPI_CLIENT_TOKEN,
                        "Content-Type": "application/json"}

    def send(self, message, phone) -> None:
        # Envia a mensagem
        payload: dict = {"phone": phone,
                   "message": message}
        requests.post(self.url, json=payload, headers=self.headers)

