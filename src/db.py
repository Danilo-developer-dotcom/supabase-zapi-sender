from dotenv import load_dotenv
from supabase import create_client, Client
import os


class Supabase:
    def __init__(self):
        # Carrega as variáveis de ambiente e conecta ao Banco de Dados
        load_dotenv()
        self.SUPABASE_URL: str = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def read(self):
        # Faz a leitura das colunas do Banco de Dados e converte formato Json para dicionário Python
        data = self.supabase.table("contatos").select("nome, telefone").execute().data
        return data