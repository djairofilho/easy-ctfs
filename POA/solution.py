import requests

URL = "http://ctf.darkautomation.com.br:32774/"

# 1) pega cookie original da instância atual
s = requests.Session()
r = s.get(URL)
orig_cookie = s.cookies.get("auth")
print("[+] cookie original:", orig_cookie)

raw = bytes.fromhex(orig_cookie)
iv = bytearray(raw[:16])
rest = raw[16:]  # C1|C2...

# 2) primeiro bloco conhecido
orig_p1 = b"user:guest|info:"
tgt_p1  = b"user:admin|info:"

# 3) bit-flip no IV para forjar P1
for i in range(16):
    iv[i] ^= orig_p1[i] ^ tgt_p1[i]

forged_cookie = (bytes(iv) + rest).hex()
print("[+] cookie forjado:", forged_cookie)

# 4) envia cookie forjado
r2 = requests.get(URL, cookies={"auth": forged_cookie})
print("[+] status:", r2.status_code)
print("[+] body:", r2.text)