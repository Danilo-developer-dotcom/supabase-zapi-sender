from src.db import Supabase
from src.zapi import Zapi

supabase = Supabase()
zapi = Zapi()

contacts_list = supabase.read()

for contact in contacts_list:
    name = contact["name"]
    phone = contact["phone"]
    message = f"Olá, {name} tudo bem com você?"
    zapi.send(message, phone)

