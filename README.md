# supabase-zapi-sender

Código Python que faz a leitura de contatos do Supabase e envia
mensagens personalizadas via Z-API (Whatsapp)
---
## Tecnologias utilizadas
 - Python
 - Supabase (Banco de Dados)
 - Z-API (Envio de mensagem por Whatsapp)
---
No Supabase, crie a seguinte tabela em seu Banco de Dados:

````commandline
create table contacts(
  id serial primary key,
  name varchar(50) not null,
  phone varchar(30) unique not null,
  created_at timestamp default now()
)
````
O campo `phone` deve conter o DDI + DDD + número, sem símbolos ou espaçamentos. Exemplo: `5511999999999`

---
## Variáveis de Ambiente

Copie o arquivo como no exemplo a seguir e preencha com suas credenciais
```bash
cp .env.example .env
```

---
- `SUPABASE_URL`: Painel do Supabase → Project Settings → API
- `SUPABASE_KEY`: Painel do Supabase → Project Settings → API
- `ZAPI_ID`: Painel da Z-API → sua instância
- `ZAPI_TOKEN`: Painel da Z-API → sua instância
- `ZAPI_CLIENT_TOKEN`: Painel da Z-API → Security

---

## Como Rodar

- 1º Clone o repositório:

```bash
git clone https://github.com/Danilo-developer-dotcom/supabase-zapi-sender.git
cd supabase-zapi-sender
```

- 2º instale as dependências:
```bash
pip install -r requirements.txt
```

- 3º Configure o `.env` conforme instruções acima.

- 4º Execute:
```bash
python main.py
```

---

## Função dos Módulos

`db.py`: Estabelece uma conexão com o Supabase, acessando
os dados da tabela `contacts` através do método `read()`.

`zapi.py`: Acessa a Z-API pela biblioteca `requests`, utilizando do método
`send` para o envio das mensagens personalizadas.

`main.py`: Acessa individualmente os módulos `db.py` e `zapi.py` para a
devida integração e utilização de seus métodos.



