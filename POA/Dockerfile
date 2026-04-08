FROM python:3.9-slim

RUN pip install flask pycryptodome

WORKDIR /app
COPY app.py .

# O GZCTF lida com a variável FLAG automaticamente
EXPOSE 8080

CMD ["python", "app.py"]