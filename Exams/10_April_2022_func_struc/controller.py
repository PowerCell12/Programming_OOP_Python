from project.player import Player
from project.supply.food import Food
from project.supply.drink import Drink
from project.supply.supply import Supply

class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []



    def add_player(self, *args):

        added = []
        for player in args:

            if player not in self.players:
                self.players.append(player)
                added.append(player)

        return f"Successfully added: {', '.join([m.name for m in added])}"


    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)



    def sustain(self, player_name: str, sustenance_type: str):

        if sustenance_type != "Drink" and sustenance_type != "Food":
            pass
        elif player_name not in [n.name for n in self.players]:
            pass
        else:

            player = None
            for p in self.players:
                if p.name == player_name:
                    player = p
                    break

            if player.stamina == 100:
                return f"{player_name} have enough stamina."


            if sustenance_type == "Drink":
                bool1 = False
                for food in self.supplies:
                    if food.__class__.__name__ == "Drink":
                        bool1 =True

                if not bool1:
                    raise Exception("There are no drink supplies left!")

            elif sustenance_type == "Food":
                bool1 = False
                for food in self.supplies:
                    if food.__class__.__name__ == "Food":
                        bool1 =True

                if not bool1:
                    raise Exception("There are no food supplies left!")



            for i in range(len(self.supplies) - 1, - 1, -1):

                if self.supplies[i].__class__.__name__ == sustenance_type:
                    supply = self.supplies.pop(i)
                    if player.stamina  +supply.energy > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy

                    return f"{player_name} sustained successfully with {supply.name}."




    def duel(self, first_player_name: str, second_player_name: str):

        player1 = None
        player2 = None
        for p in self.players:
            if p.name == first_player_name:
                player1 = p
            elif p.name == second_player_name:
                player2 = p


        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\nPlayer {player2.name} does not have enough stamina."

        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."

        starting_player = None
        second = None
        if player1.stamina < player2.stamina:
            second = player2
            starting_player = player1
        else:
            second = player1
            starting_player = player2

        if second.stamina - starting_player.stamina / 2 <= 0:
            second.stamina = 0
            return f"Winner: {starting_player.name}."

        second.stamina -= starting_player.stamina / 2


        if starting_player.stamina - second.stamina / 2 <= 0:
            starting_player.stamina = 0
            return f"Winner: {second.name}."

        starting_player.stamina -= second.stamina / 2



        if starting_player.stamina > second.stamina:
                return f"Winner: {starting_player.name}."
        elif starting_player.stamina < second.stamina:
            return f"Winner: {second.name}."


    def next_day(self):

        for i in range(len(self.players)):
            person = self.players[i]
            if person.stamina - person.age * 2 < 0:
                person.stamina = 0
            else:
                person.stamina -= person.age  * 2

            self.sustain(person.name, "Food")
            self.sustain(person.name, "Drink")


    def __str__(self):
        list = []
        for person in self.players:
            list.append(str(person))

        for supply in self.supplies:
            list.append(supply.details())

        return "\n".join(list)
