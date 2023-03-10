# cnab-transactions

O CNAB (Centro Nacional de Automação Bancária) é um instrumento de digitalização, integração e automação da comunicação entre bancos, empresas e clientes. Com o CNAB, uma empresa envia e recebe informações financeiras sobre o registro de pagamentos, facilitando a gestão de suas finanças.

Esse projeto tem como intuito salvar informações referentes à transações financeiras, de estabelecimentos comerciais, em um banco de dados através do parseamento e a normalização das informações recebidas via arquivo `txt`.

## Tecnologias utilizadas

Django, Django REST-Framework, Django-oauth e PostgreSQL

Para testar a aplicação, faça o clone do repositório para sua máquina e em seguida realize os passos abaixo.

## Executando a aplicação

### Usando docker

1. No terminal execute o comando:

   ```bash
   docker compose up
   ```

2. Abra o navegador e acesse o endereço:

   ```bash
   localhost:8000/api/cnab_file/
   ```

   Faça uma cópia do arquivo `CNAB.txt` que se encontra no diretório test_dataframe. Ele serve para ser enviado no formulário da página acessada. As transações serão listadas na tela.

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
