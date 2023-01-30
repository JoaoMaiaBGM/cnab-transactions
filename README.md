# cnab-transactions

Para testar a aplicação, fala o clone do repositório para sua máquina e em seguida realize os passos abaixo.

## Usando docker

1. No terminal execute o comando:

   ```bash
   docker compose up
   ```

2. Abra o Chrome e acesse o endereço:

   ```bash
   localhost:8000/api/cnab_file/
   ```

   Faça uma cópia do arquivo `CNAB.txt` que se encontra no diretório test_dataframe. Ele serve para ser enviado no fomrulário da página acessada. As transações serão listadas na tela.

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
