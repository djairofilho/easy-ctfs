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

## Padrao de branch

Crie branches curtas e descritivas, sempre em minusculo e separadas por `-`.

Formato recomendado:

`<tipo>/<escopo>-<descricao-curta>`

Tipos recomendados para branch:

- `feat/`
- `fix/`
- `refactor/`
- `docs/`
- `chore/`

Exemplos:

- `feat/poa-cookie-hardening`
- `fix/poa-invalid-cookie-handling`
- `docs/repo-ctf-catalog`
- `refactor/repo-structure`

## Padrao de pull request (PR)

Abra PR de branch para `main` com foco em uma mudanca unica.

Checklist sugerido:

- titulo alinhado com Conventional Commits (mesmo estilo dos commits)
- descricao com contexto, mudanca principal e impacto
- passos de validacao (como testar localmente)
- referencia a issue/tarefa, quando existir

Boas praticas:

- prefira PRs pequenas e revisaveis
- evite misturar refactor + feature + docs na mesma PR
- mantenha a branch atualizada com `main` antes de solicitar review

## Estrutura esperada por desafio

Cada pasta de CTF deve conter:

- `README.md` com setup local, execucao e uso no CTF
- codigo da aplicacao (ex.: `app.py`)
- script de solucao/exploit (ex.: `solution.py`)
- `Dockerfile` para deploy

## Documentacao

- A raiz do repositorio concentra visao geral e catalogo.
- Cada CTF concentra detalhes tecnicos e passo a passo proprio.
