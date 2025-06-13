# Git for Developer

Uma ferramenta para ajudar desenvolvedores a trabalhar com Git de forma mais eficiente.

## Requisitos

- Python 3.8 ou superior
- Git instalado no sistema

## Instalação

### Instalação Local (Recomendada para Desenvolvimento)

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

### Instalação Global (Recomendada para Uso)

Para instalar o comando `gfd` globalmente no seu sistema:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/git-for-developer.git
cd git-for-developer
```

2. Instale o pacote em modo de desenvolvimento:
```bash
pip install -e .
```

Após a instalação, você poderá usar o comando `gfd` de qualquer diretório do seu sistema.

## Funcionalidades

- Criação automática de branches de feature com o padrão `feature/NUMERO_DEMANDA/NOME_DA_DEMANDA`
- Pull automático da branch master antes de criar uma nova feature
- Atualização automática da branch de feature com a master
- Envio automático da branch para o servidor remoto
- Listagem de todas as branches de feature e bug com opção de troca entre elas

## Como usar

### Se instalado globalmente:
```bash
gfd <comando> [argumentos]
```

### Se usando localmente:
```bash
python gfd.py <comando> [argumentos]
```

Comandos disponíveis:

Para criar uma nova feature:
```bash
gfd create <numero_demanda> <nome_demanda>
```

Para atualizar sua feature com a master:
```bash
gfd update
```

Para enviar sua branch para o servidor:
```bash
gfd push
```

Para listar todas as branches de feature e bug e trocar entre elas:
```bash
gfd list
```

## Fluxo de Trabalho Recomendado

1. Crie uma nova feature:
   ```bash
   gfd create 123 "nome-da-demanda"
   ```

2. Faça suas alterações e commits localmente

3. Quando quiser atualizar sua branch com a master:
   ```bash
   gfd update
   ```

4. Quando quiser enviar suas alterações para o servidor:
   ```bash
   gfd push
   ```

5. Para listar e trocar entre diferentes demandas:
   ```bash
   gfd list
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