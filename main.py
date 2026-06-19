from src.db import Supabase
from src.zapi import Zapi
from dotenv import load_dotenv

load_dotenv()
supabase = Supabase()
zapi = Zapi()

contacts_list = supabase.read()  # lista de contatos em formato de dicionário

for contact in contacts_list:
    message = f"Olá, {contact["name"]} tudo bem com você?"
    zapi.send(message, contact["phone"])
