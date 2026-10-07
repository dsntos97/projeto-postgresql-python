# Banco de Dados

## PostgreSQL

Banco utilizado no projeto:

- PostgreSQL
- Host: localhost
- Porta: 5432
- Banco: thinkerguy

## SQLAlchemy

SQLAlchemy é utilizado como camada de acesso ao banco e ORM.

## Alembic

Alembic controla a evolução do schema do banco através de migrations.

## Primeira migration

A primeira migration cria a tabela `talhoes`.

Estrutura inicial:

- `id`: chave primária
- `nome`: nome do talhão
- `area_hectares`: área em hectares
- `cultura`: cultura plantada

## Comandos úteis

Verificar estado:

```bash
alembic current
