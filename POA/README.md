# POA - Padding Oracle Attack (CTF)

Desafio de CTF em Flask com cookie AES-CBC vulneravel a bit-flipping/padding oracle para obter privilegio de admin e revelar a flag.

## Estrutura

- `app.py`: aplicacao Flask do desafio
- `Dockerfile`: imagem para deploy (porta `8080`)
- `solution.py`: script de exploracao do desafio
- `.gitignore`: regras de arquivos locais
- `CONTRIBUTING.md`: padrao de commits (`feat`, `fix`, `chore`)

## Como executar localmente

1. Instale dependencias Python:

```bash
pip install flask pycryptodome requests
```

2. Rode a aplicacao:

```bash
python app.py
```

3. Acesse no navegador:

```text
http://localhost:8080/
```

Por padrao local, a flag fallback e `flag{teste_local_123}` se a variavel `FLAG` nao estiver definida.

## Executar com Docker

Build da imagem:

```bash
docker build -t poa:latest .
```

Rodar local:

```bash
docker run --rm -p 8080:8080 -e FLAG="flag{teste_docker}" poa:latest
```

## Publicacao no Docker Hub

Exemplo com o repositorio `djairodsf/poa-ctf`:

```bash
docker tag poa:latest djairodsf/poa-ctf:latest
docker push djairodsf/poa-ctf:latest
```

## Uso no GZCTF

No desafio dinamico/container:

- Image: `djairodsf/poa-ctf:latest`
- Porta do servico: `8080`
- Flag: preencher no campo de flag do proprio GZCTF

O app ja le a flag por variavel de ambiente `FLAG`.

## Solucao (exploit)

O arquivo `solution.py` demonstra um ataque de bit-flip no IV do cookie `auth` para transformar `user:guest` em `user:admin` e obter a flag.

Execucao:

```bash
python solution.py
```

> Ajuste a constante `URL` em `solution.py` para a instancia alvo.
