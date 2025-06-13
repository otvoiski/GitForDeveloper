#!/usr/bin/env python3
import sys
import os
from git import Repo
from colorama import init, Fore, Style
import re

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

def list_branches():
    repo = get_current_repo()
    
    try:
        # Obtém todas as branches locais
        branches = [branch.name for branch in repo.heads]
        
        # Filtra apenas branches de feature e bug
        feature_branches = []
        bug_branches = []
        
        for branch in branches:
            if branch.startswith('feature/'):
                feature_branches.append(branch)
            elif branch.startswith('bug/'):
                bug_branches.append(branch)
        
        if not feature_branches and not bug_branches:
            print_info("Não foram encontradas branches de feature ou bug.")
            return
        
        print_info("\nSelecione a demanda que deseja mudar:")
        
        # Lista branches de feature
        for i, branch in enumerate(feature_branches, 1):
            parts = branch.split('/')
            if len(parts) >= 3:
                numero = parts[1]
                titulo = ' '.join(parts[2:]).replace('_', ' ').title()
                print(f"{i}. [{Fore.GREEN}FEATURE{Style.RESET_ALL}] [{numero}] - {titulo}")
        
        # Lista branches de bug
        for i, branch in enumerate(bug_branches, len(feature_branches) + 1):
            parts = branch.split('/')
            if len(parts) >= 3:
                numero = parts[1]
                titulo = ' '.join(parts[2:]).replace('_', ' ').title()
                print(f"{i}. [{Fore.RED}BUG{Style.RESET_ALL}] [{numero}] - {titulo}")
        
        # Solicita seleção do usuário
        while True:
            try:
                choice = int(input("\nDigite o número da demanda (ou 0 para cancelar): "))
                if choice == 0:
                    return
                
                all_branches = feature_branches + bug_branches
                if 1 <= choice <= len(all_branches):
                    selected_branch = all_branches[choice - 1]
                    switch_to_branch(selected_branch)
                    break
                else:
                    print_error("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print_error("Por favor, digite um número válido.")
        
    except Exception as e:
        print_error(f"Erro ao listar branches: {str(e)}")
        sys.exit(1)

def switch_to_branch(branch_name):
    repo = get_current_repo()
    
    try:
        # Verifica se há alterações não commitadas
        if repo.is_dirty():
            print_error("Existem alterações não commitadas. Por favor, faça commit das suas alterações primeiro.")
            sys.exit(1)
        
        print_info(f"Trocando para a branch {branch_name}...")
        repo.git.checkout(branch_name)
        print_success(f"Trocou com sucesso para a branch {branch_name}")
        
    except Exception as e:
        print_error(f"Erro ao trocar de branch: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print_error("Uso: gfd <comando> [argumentos]")
        print_info("Comandos disponíveis:")
        print_info("  create <numero_demanda> <nome_demanda> - Cria uma nova branch de feature")
        print_info("  update - Atualiza a branch atual com a master")
        print_info("  push - Envia a branch atual para o servidor")
        print_info("  list - Lista todas as branches de feature e bug e permite trocar entre elas")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'create':
        if len(sys.argv) != 4:
            print_error("Uso: gfd create <numero_demanda> <nome_demanda>")
            sys.exit(1)
        create_feature_branch(sys.argv[2], sys.argv[3])
    
    elif command == 'update':
        update_feature_branch()
    
    elif command == 'push':
        push_feature_branch()
    
    elif command == 'list':
        list_branches()
    
    else:
        print_error(f"Comando desconhecido: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main() 