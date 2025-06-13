#!/usr/bin/env python3
import sys
import os
from git import Repo
from colorama import init, Fore, Style

# Inicializa o colorama para Windows
init()

def print_success(message):
    print(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")

def print_info(message):
    print(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")

def get_current_repo():
    try:
        return Repo('.')
    except Exception as e:
        print_error("Não foi possível encontrar um repositório Git válido no diretório atual.")
        sys.exit(1)

def create_feature_branch(numero_demanda, nome_demanda):
    repo = get_current_repo()
    
    # Formata o nome da branch
    branch_name = f"feature/{numero_demanda}/{nome_demanda.lower().replace(' ', '_')}"
    
    print_info(f"Criando nova branch: {branch_name}")
    
    try:
        # Atualiza a master
        print_info("Atualizando branch master...")
        repo.git.checkout('master')
        repo.git.pull()
        
        # Cria e muda para a nova branch
        print_info(f"Criando branch {branch_name}...")
        new_branch = repo.create_head(branch_name)
        new_branch.checkout()
        
        print_success(f"Branch {branch_name} criada com sucesso!")
        
    except Exception as e:
        print_error(f"Erro ao criar branch: {str(e)}")
        sys.exit(1)

def update_feature_branch():
    repo = get_current_repo()
    
    try:
        # Obtém o nome da branch atual
        current_branch = repo.active_branch.name
        
        if current_branch == 'master':
            print_error("Você está na branch master. Por favor, mude para uma branch de feature primeiro.")
            sys.exit(1)
        
        print_info(f"Atualizando branch {current_branch}...")
        
        # Salva alterações locais
        if repo.is_dirty():
            print_info("Salvando alterações locais...")
            repo.git.stash()
            has_stash = True
        else:
            has_stash = False
        
        # Atualiza a master
        print_info("Atualizando master...")
        repo.git.checkout('master')
        repo.git.pull()
        
        # Volta para a branch de feature e faz merge
        print_info(f"Fazendo merge com master na branch {current_branch}...")
        repo.git.checkout(current_branch)
        repo.git.merge('master')
        
        # Restaura alterações locais se necessário
        if has_stash:
            print_info("Restaurando alterações locais...")
            repo.git.stash.pop()
        
        print_success(f"Branch {current_branch} atualizada com sucesso!")
        
    except Exception as e:
        print_error(f"Erro ao atualizar branch: {str(e)}")
        sys.exit(1)

def push_feature_branch():
    repo = get_current_repo()
    
    try:
        # Obtém o nome da branch atual
        current_branch = repo.active_branch.name
        
        if current_branch == 'master':
            print_error("Você está na branch master. Por favor, mude para uma branch de feature primeiro.")
            sys.exit(1)
        
        print_info(f"Enviando branch {current_branch} para o servidor...")
        
        # Verifica se há alterações não commitadas
        if repo.is_dirty():
            print_error("Existem alterações não commitadas. Por favor, faça commit das suas alterações primeiro.")
            sys.exit(1)
        
        # Verifica se há commits locais não enviados
        local_commits = list(repo.iter_commits(f'{current_branch}@{{u}}..{current_branch}'))
        if not local_commits:
            print_info("Não há commits novos para enviar.")
            return
        
        # Envia a branch para o servidor
        print_info(f"Enviando {len(local_commits)} commit(s) para o servidor...")
        repo.git.push('origin', current_branch)
        
        print_success(f"Branch {current_branch} enviada com sucesso para o servidor!")
        
    except Exception as e:
        print_error(f"Erro ao enviar branch: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print_error("Uso: python git_for_developer.py <comando> [argumentos]")
        print_info("Comandos disponíveis:")
        print_info("  create <numero_demanda> <nome_demanda> - Cria uma nova branch de feature")
        print_info("  update - Atualiza a branch atual com a master")
        print_info("  push - Envia a branch atual para o servidor")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'create':
        if len(sys.argv) != 4:
            print_error("Uso: python git_for_developer.py create <numero_demanda> <nome_demanda>")
            sys.exit(1)
        create_feature_branch(sys.argv[2], sys.argv[3])
    
    elif command == 'update':
        update_feature_branch()
    
    elif command == 'push':
        push_feature_branch()
    
    else:
        print_error(f"Comando desconhecido: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main() 