from supabase import create_client, Client
import os


class Supabase:
    def __init__(self):
        # Carrega as variáveis de ambiente e conecta ao Banco de Dados
        self.SUPABASE_URL: str = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

        # Validação de variáveis de ambiente
        if not self.SUPABASE_KEY or not self.SUPABASE_URL:
            raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY são obrigatórias.")
        self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def read(self) -> list:
        # Faz a leitura das colunas do Banco de Dados e converte formato Json para dicionário Python
        data = self.supabase.table("contacts").select("name, phone").execute().data
        return data
