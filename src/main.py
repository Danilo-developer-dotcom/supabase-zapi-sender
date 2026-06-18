from src.db import Supabase

supabase = Supabase()

lista_contatos = supabase.read()