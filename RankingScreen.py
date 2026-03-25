import os
import json

TeamsHistory = "teams.json"

#Funções utilizadas no código-----------------------------------------------
def clear():
    os.system('cls')
def load_teams():
    if os.path.exists(TeamsHistory):
        with open(TeamsHistory, "r") as f:
            return json.load(f)
    return []

def save_teams(teams):
    with open(TeamsHistory, "w") as f:
        json.dump(teams, f)

def create_teams(names):
    return {"nome": names, "pontos": 0}

def add_points(teams):
    while True:
        clear()
        print("=== PONTUAÇÃO ===")
        for i, team in enumerate(teams, start=1):
            print(f"  {i}. {team['nome']} - {team['pontos']} pontos")
        
        print("\nO que deseja fazer?")
        print("  1. Adicionar pontos")
        print("  2. Encerrar e ver ranking final")
        
        option = input("\nEscolha uma opção: ")
        
        if option == '1':
            number = int(input("Digite o número da equipe: "))
            if 1 <= number <= len(teams):
                points = int(input("Quantos pontos?: "))
                teams[number - 1]['pontos'] += points
                save_teams(teams)
                print(f"Pontos adicionados com sucesso!")
            else:
                print("Equipe inválida!")
        
        elif option == '2':
            clear()
            print("=== RANKING FINAL ===")
            ranking = sorted(teams, key=lambda x: x['pontos'], reverse=True)
            for i, team in enumerate(ranking, start=1):
                print(f"  {i}. {team['nome']} - {team['pontos']} pontos")
            break

#Código principal-------------------------------------

teams = load_teams()

clear()

if len(teams) == 0:
    answear = input("Nenhuma equipe registrada, deseja registrar equipes? (S/N): ")
    if answear == 'S' or answear == 's':
        print("\nVamos registrar nossas equipes!")
        
        while True:
            name = input("Digite o nome da equipe (ou 'sair' para terminar): ")
            if name.lower() == 'sair':
                break
            newTeam = create_teams(name)
            teams.append(newTeam)
        
        save_teams(teams)
        print("Equipes registradas com sucesso!")
    else:
        print("Até mais!")
else:
    print("Equipes registradas:")
    for i, team in enumerate(teams, start=1):
        print(f"  {i}. {team['nome']} - {team['pontos']} pontos")
    
    answear = input("\nDeseja continuar a pontuação dessas equipes? (S/N): ")
    if answear == 'S' or answear == 's':
        print("Continuando pontuação!")
        add_points(teams)
    else:
        print("Até mais!")
    