

class BasketballTeam:
    def __init__(self):
        self.players = []
        self.ages = []

    def add_player(self, name, age):
        self.players.append(name)
        self.ages.append(age)

    def display_team_info(self):
        print("Players:")
        for i in range(len(self.players)):
            print(f"{self.players[i]} ({self.ages[i]})")


# Create a new FootballTeam object
team = BasketballTeam()

# Add players to the team
team.add_player("Devin Booker", 26)
team.add_player("Anthony Edwards", 22)
team.add_player("Stephen Curry", 35)
team.add_player("Nikola Jokic", 28)

# Display the team info
team.display_team_info()


# Zadanie 1: dodaj metodę remove_player()
# Zadanie 2: update_player_age()
# Zadanie 3: get_youngest_player()
# Zadanie 4: Poproś ChatGPT o sugestie dotyczące poprawy kodu
