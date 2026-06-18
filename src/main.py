from src.db import Supabase
from src.zapi import Zapi
from dotenv import load_dotenv

load_dotenv()
supabase = Supabase()
zapi = Zapi()

# lista de contatos em formato de dicionário
contacts_list = supabase.read()

for contact in contacts_list:
    message = f"Olá, {contact["name"]} tudo bem com você?"
    zapi.send(message, contact["phone"])
