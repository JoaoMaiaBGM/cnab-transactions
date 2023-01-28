# cnab-transactions

## Usando docker

1. No terminal execute o comando:

   ```bash
   docker compose up
   ```

2. Abra o Chrome e acesse o endereço:

   ```bash
   localhost:8000/api/cnab_file/
   ```

   Selecione o arquivo `CNAB` de extensão `.txt` a ser enviado. As transações serão listadas na tela.

   Após listagem, caso queira alternar entre telas, acesse o endereço:

   ```bash
   localhost:8000/api/cnab_file/

               ou

   localhost:8000/api/cnab_file/transactions/
   ```

---

## Usando seu ambiente virtual

### Iniciando a aplicação

1. Crie seu ambiente virtual:

   ```bash
   python -m venv venv
   ```

2. Ative seu ambiente (venv):

   ```bash
   # Linux:
   source venv/bin/activate
   ```

   ```bash
   # Windows:
   .\venv\Scripts\activate

   ```

3. Instale os pacotes do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode as migrations:

   ```bash
   python manage.py migrate
   ```
