# cnab-transactions

## Iniciando a aplicação

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
