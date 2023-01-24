FROM python:3.11

# Não utilizar arquivos .pyc na cronstução da imagem/criação container
ENV PYTHONDONTWRITEBYTECODE 1

# Salva os logs de erros
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -U pip
RUN pip install -r requirements.txt