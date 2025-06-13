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

## Como usar

1. Ative o ambiente virtual (se ainda não estiver ativo):
```bash
# No Windows
.venv\Scripts\activate

# No Linux/Mac
source .venv/bin/activate
```

2. Execute o script:
```bash
python git_for_developer.py
```

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