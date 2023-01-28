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

3. Caso queira remover o banco e/ou o container, execute no terminal:
   ```bash
   docker compose down
   ```

---
