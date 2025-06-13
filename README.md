# Git for Developer

Uma ferramenta para ajudar desenvolvedores a trabalhar com Git de forma mais eficiente.

## Requisitos

- Python 3.8 ou superior
- Git instalado no sistema

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/git-for-developer.git
cd git-for-developer
```

2. Crie um ambiente virtual (venv):
```bash
# No Windows
python -m venv .venv
.venv\Scripts\activate

# No Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Funcionalidades

- Criação automática de branches de feature com o padrão `feature/NUMERO_DEMANDA/NOME_DA_DEMANDA`
- Pull automático da branch master antes de criar uma nova feature
- Atualização automática da branch de feature com a master
- Envio automático da branch para o servidor remoto
- Listagem de todas as branches de feature e bug
- Troca fácil entre diferentes branches de feature e bug

## Como usar

1. Ative o ambiente virtual (se ainda não estiver ativo):
```bash
# No Windows
.venv\Scripts\activate

# No Linux/Mac
source .venv/bin/activate
```

2. Execute o script com os seguintes comandos:

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

Para listar todas as branches de feature e bug:
```bash
python git_for_developer.py list
```

Para trocar para outra branch de feature ou bug:
```bash
python git_for_developer.py switch
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

5. Para trocar entre diferentes demandas:
   ```bash
   python git_for_developer.py switch
   ```
   - Selecione a demanda desejada na lista numerada
   - Digite 0 para cancelar a operação

## Desenvolvimento

Para contribuir com o projeto:

1. Crie uma branch para sua feature:
```bash
git checkout -b feature/nova-funcionalidade
```

2. Faça suas alterações e commit:
```bash
git add .
git commit -m "Adiciona nova funcionalidade"
```

3. Envie suas alterações:
```bash
git push origin feature/nova-funcionalidade
```

## Licença

Este projeto está sob a licença MIT.