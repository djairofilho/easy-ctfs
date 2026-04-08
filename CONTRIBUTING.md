# Guia de contribuicao

## Padrao de commit

Use Conventional Commits com formato:

`type(scope): short summary`

Tipos recomendados neste repositorio:

- `feat`: nova funcionalidade
- `fix`: correcao de bug
- `refactor`: mudanca estrutural sem alterar comportamento esperado
- `docs`: documentacao
- `chore`: manutencao/tooling

Exemplos:

- `feat(poa): add vulnerable auth cookie challenge`
- `fix(poa): handle malformed hex cookie gracefully`
- `refactor(repo): reorganize challenge files into POA directory`
- `docs(repo): add root CTF catalog and contribution guide`

## Estrutura esperada por desafio

Cada pasta de CTF deve conter:

- `README.md` com setup local, execucao e uso no CTF
- codigo da aplicacao (ex.: `app.py`)
- script de solucao/exploit (ex.: `solution.py`)
- `Dockerfile` para deploy

## Documentacao

- A raiz do repositorio concentra visao geral e catalogo.
- Cada CTF concentra detalhes tecnicos e passo a passo proprio.
