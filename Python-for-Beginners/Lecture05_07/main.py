## Code Challenge

# Basic Class
class Player:
    # init method that is get parameter from outside
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    # print
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

nico = Player(name = "Nico", team = "Team X")
nico.introduce()

lynn = Player(name = "Lynn", team = "Team Blue")
lynn.introduce()

# Add new class 'Team'
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)


team_x = Team("Team X")
team_x.add_player("Nico")

team_blue = Team("Team Blue")
team_blue.add_player("Lynn")

print(team_blue.players) # print Object address in memory

# Add method for display property to string
class Team2:
    def __init__(self, team_name):
            self.team_name = team_name
            self.players = []

    # New Method
    def show_players(self):
        # Loop self.players
        for player in self.players:
            # Each element in players has structure of class Player
            # => each player has Method introduce()
            player.introduce()
    
    def add_player(self, name):
        # when create new_player, property has structure of Class Player
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

team_x_2 = Team2("Team X")
team_x_2.add_player("Nico")

team_x_2.show_players()