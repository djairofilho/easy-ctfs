# Repositorio de CTFs

Colecao de desafios para estudos de seguranca ofensiva no InsperSec.

## Objetivo

- Centralizar desafios em uma estrutura unica e padronizada.
- Facilitar execucao local, empacotamento em container e deploy em plataformas de CTF.

## Estrutura do repositorio

Cada CTF deve ficar em uma pasta propria:

```text
ctfs/
  <NOME_DO_CTF>/
    app.py
    solution.py
    Dockerfile
    README.md
    CONTRIBUTING.md
```

## Catalogo de desafios

- `POA/`: desafio de criptografia com falha em cookie AES-CBC (bit-flip/padding oracle).

## Como usar

1. Entre na pasta do desafio desejado.
2. Siga as instrucoes do `README.md` do proprio desafio.
3. Se precisar de padroes de commit, consulte `CONTRIBUTING.md`.

## Convencoes

- Commits em Conventional Commits: `type(scope): resumo`.
- Tipos principais: `feat`, `fix`, `chore`, `refactor`, `docs`.
- Documentacao geral fica na raiz e documentacao tecnica fica dentro de cada CTF.

## Adicionando um novo CTF

- Crie uma nova pasta na raiz com nome curto e descritivo.
- Inclua no minimo `README.md` com setup, execucao e estrategia de solucao.
- Atualize o catalogo deste arquivo com o novo desafio.
