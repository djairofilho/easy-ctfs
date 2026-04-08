# POA - Padding Oracle / CBC Bit-Flipping (CTF)

Desafio web em Flask com autenticacao por cookie AES-CBC vulneravel, permitindo elevar privilegio de `guest` para `admin` e capturar a flag.

## Objetivo do desafio

Explorar o cookie `auth` para alterar o plaintext descriptografado sem conhecer a chave, usando manipulacao de bits no IV (e comportamento de erro de padding como sinal auxiliar).

## Arquivos

- `app.py`: servico vulneravel
- `solution.py`: exploit de referencia
- `Dockerfile`: empacotamento para deploy
- `.gitignore`: regras locais de Python/editor
- `CONTRIBUTING.md`: convencoes de commit deste CTF

## Vulnerabilidade resumida

- O app cifra o cookie com AES-CBC.
- O primeiro bloco de plaintext e previsivel: `user:guest|info:`.
- Em CBC, alterar bytes do IV altera bytes do primeiro bloco apos decrypt.
- Com bit-flipping no IV, o atacante forja `user:admin|info:` sem conhecer a chave.

## Setup local

1. Instale dependencias:

```bash
pip install flask pycryptodome requests
```

2. Execute o servidor:

```bash
python app.py
```

3. Acesse:

```text
http://localhost:8080/
```

Variaveis importantes:

- `FLAG`: flag retornada para admin
- fallback local: `flag{teste_local_123}`

## Execucao com Docker

Build:

```bash
docker build -t poa:latest .
```

Run:

```bash
docker run --rm -p 8080:8080 -e FLAG="flag{teste_docker}" poa:latest
```

## Deploy em plataforma CTF (ex.: GZCTF)

- Imagem: `djairodsf/poa-ctf:latest`
- Porta exposta: `8080`
- Flag: configurada no campo da plataforma

O servico ja le a flag por variavel de ambiente `FLAG`.

## Solucao de referencia

O `solution.py` executa:

1. Requisita `/` para obter cookie `auth` legitimo.
2. Separa `IV | C1 | C2...`.
3. Aplica XOR no IV para transformar `user:guest|info:` em `user:admin|info:`.
4. Reenvia cookie forjado e le resposta com a flag.

Execucao:

```bash
python solution.py
```

Antes de rodar, ajuste a constante `URL` no arquivo `solution.py` para a instancia alvo.

## Troubleshooting rapido

- `500 Padding Error`: cookie invalido ou bytes alterados incorretamente.
- `400 Erro interno`: formato do cookie nao esperado.
- Sem flag na resposta: forja nao gerou substring `admin` no plaintext final.

## Aviso etico

Use este material apenas em ambiente controlado de ensino/CTF autorizado.
