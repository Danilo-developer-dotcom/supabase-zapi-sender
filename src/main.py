from src.db import Supabase
from src.zapi import Zapi

supabase = Supabase()
zapi = Zapi()

contacts_list = supabase.read()

for i in range(len(contacts_list)):
    name = contacts_list[i]["name"]
    phone = contacts_list[i]["phone"]
    message = f"Olá, {name} tudo bem com você?"
    zapi.send(message, phone)

