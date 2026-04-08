from flask import Flask, request, make_response, render_template_string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
# O GZCTF injeta a FLAG como variável de ambiente
FLAG = os.getenv("FLAG", "flag{teste_local_123}")
KEY = os.urandom(16)

def encrypt(text):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(text.encode(), 16))
    return (iv + ct).hex()

def decrypt(hex_data):
    data = bytes.fromhex(hex_data)
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), 16)

@app.route('/')
def index():
    auth = request.cookies.get('auth')
    if not auth:
        # Define um cookie inicial para o jogador
        resp = make_response("🍪")
        resp.set_cookie('auth', encrypt("user:guest|info:nada_aqui"))
        return resp
    
    try:
        decrypted = decrypt(auth)
        if b"admin" in decrypted:
            return f"Olá Admin! Aqui está sua flag: {FLAG}"
        return f"Olá usuário comum. Seu conteúdo é: {decrypted.decode()}"
    except ValueError:
        # O segredo do desafio: O servidor retorna 500 se o padding estiver errado
        return "Erro de preenchimento (Padding Error)!", 500
    except Exception:
        return "Erro interno", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)