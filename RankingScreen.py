import os
import json

TeamsHistory = "teams.json"

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

#Código principal-------------------------------------

teams = load_teams()

clear()

if len(teams) == 0:
    answear = input("Nenhuma equipe registrada, deseja registrar equipes? (S/N): ")
    if answear == 'S' or answear == 's':
        print("Vamos registrar nossas equipes!")
        
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
    print("Equipes existem já!")
    