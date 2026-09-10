## Why We Need OOP

# Dictionary for User
nico = {
    "name" : "Nico",
    "XP" : 1000,
    "team" : "Team X"
}

# Function of print user info.
def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello, My name is {name} and I play for {team}")

# execute
introduct_player(nico)

# create new function of create user info
def create_player(name, xp, team):
    return {
        "name" : name,
        "XP" : xp,
        "team" : team
    }

nico = create_player("Nico", 1500, "Team X")

# Due to the strong connectivity between Dictionary and Function, the structure is rigid and unusable. 
# To overcome this, the development of an OOP approach is necessary.