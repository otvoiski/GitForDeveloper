# GitForDeveloper

Uma ferramenta de linha de comando para automatizar o gerenciamento de branches Git, desenvolvida para facilitar o fluxo de trabalho dos desenvolvedores.

## Funcionalidades

- Criação automática de branches de feature com o padrão `feature/NUMERO_DEMANDA/NOME_DA_DEMANDA`
- Pull automático da branch master antes de criar uma nova feature
- Atualização automática da branch de feature com a master
- Envio automático da branch para o servidor remoto

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Para criar uma nova feature:
```bash
python git_for_developer.py create <numero_demanda> <nome_demanda>
```

Para atualizar sua feature com a master:
```bash
python git_for_developer.py update
```

Para enviar sua branch para o servidor:
```bash
python git_for_developer.py push
```

## Fluxo de Trabalho Recomendado

1. Crie uma nova feature:
   ```bash
   python git_for_developer.py create 123 "nome-da-demanda"
   ```

2. Faça suas alterações e commits localmente

3. Quando quiser atualizar sua branch com a master:
   ```bash
   python git_for_developer.py update
   ```

4. Quando quiser enviar suas alterações para o servidor:
   ```bash
   python git_for_developer.py push
   ``` 