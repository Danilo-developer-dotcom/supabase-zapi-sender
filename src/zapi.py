import os
import requests


class Zapi:
    def __init__(self):
        # Carrega as variáveis de ambiente
        self.ZAPI_ID: str = os.getenv("ZAPI_ID")
        self.ZAPI_TOKEN: str = os.getenv("ZAPI_TOKEN")
        self.ZAPI_CLIENT_TOKEN: str = os.getenv("ZAPI_CLIENT_TOKEN")

        # valida variaveis de ambiente
        if not self.ZAPI_ID or not self.ZAPI_TOKEN or not self.ZAPI_CLIENT_TOKEN:
            raise ValueError("Variáveis ZAPI_ID, ZAPI_TOKEN E ZAPI_CLIENT_TOKEN são obrigatórias.")

        # Estabelece conexão com Z-API
        self.url: str = f"https://api.z-api.io/instances/{self.ZAPI_ID}/token/{self.ZAPI_TOKEN}/send-text"
        self.headers: dict = {"Client-Token": self.ZAPI_CLIENT_TOKEN, "Content-Type": "application/json"}

    def send(self, message, phone) -> None:
        # Tenta enviar a mensagem, alertando se houver algum erro
        payload: dict = {"phone": phone, "message": message}
        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()  # lança exceção se ocorrer algum erro no envio

        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP ao enviar para {phone}: {e}")  # erros na autenticação/configurações
        except requests.exceptions.ConnectionError:
            print(f"Sem conexão ao enviar para {phone}.")  # Problema de Rede
