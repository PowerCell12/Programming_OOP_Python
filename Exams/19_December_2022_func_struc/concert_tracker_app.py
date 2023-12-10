from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts  = []


    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type != "Guitarist" and musician_type != "Drummer" and musician_type != "Singer":
                raise ValueError("Invalid musician type!")

        if name in [h.name for h in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        if musician_type == "Guitarist":
            self.musicians.append(Guitarist(name, age))
        elif musician_type == "Drummer":
            self.musicians.append(Drummer(name, age))
        elif musician_type == "Singer":
            self.musicians.append(Singer(name, age))

        return f"{name} is now a {musician_type}."



    def create_band(self, name: str):

        if name in [h.name for h in self.bands]:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."



    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):



        for con in self.concerts:
                if con.place == place:
                    raise Exception(f"{place} is already registered for {con.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."


    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician = None
        band = None
        bool1=  False
        bool2 = False

        for mus in self.musicians:
            if musician_name == mus.name:
                musician = mus
                bool1 = True
                break

        for b in self.bands:
            if band_name == b.name:
                band = b
                bool2 = True
                break

        if not bool1:
            raise Exception(f"{musician_name} isn't a musician!")

        if not bool2:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."


    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = None
        bool1 = False

        for b in self.bands:
            if band_name == b.name:
                band = b
                bool1 = True
                break

        if not bool1:
            raise Exception(f"{band_name} isn't a band!")


        musician = None

        for mus in band.members:
            if mus.name == musician_name:
                musician = mus
                break

        if musician == None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."


    def start_concert(self, concert_place: str, band_name: str):

        band = None
        for b in self.bands:
            if band_name == b.name:
                band = b
                break

        concert = None
        for con in self.concerts:
            if concert_place == con.place:
                concert = con
                break

        dict_players = {"Singer": 0, "Guitarist": 0, "Drummer": 0}

        for player in band.members:
            if player.__class__.__name__ == "Singer":
                dict_players["Singer"] += 1
            elif player.__class__.__name__ == "Guitarist":
                dict_players["Guitarist"] += 1
            elif player.__class__.__name__ == "Drummer":
                dict_players["Drummer"] += 1


        if dict_players["Drummer"] < 1 or dict_players["Guitarist"] < 1 or dict_players["Singer"] < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        bool1 = False
        if concert.genre == "Rock":

            for player in band.members:
                if player.__class__.__name__ == "Singer":

                    if "sing high pitch notes" not in player.skills:
                        bool1 = True
                        break

                elif player.__class__.__name__ == "Guitarist":

                    if "play rock" not in player.skills:
                        bool1 = True
                        break


                elif player.__class__.__name__ == "Drummer":

                    if "play the drums with drumsticks" not in player.skills:
                        bool1 = True
                        break


        elif concert.genre == "Metal":

            for player in band.members:
                if player.__class__.__name__ == "Singer":

                    if "sing low pitch notes" not in player.skills:
                        bool1 = True
                        break

                if player.__class__.__name__ == "Guitarist":

                    if "play metal" not in player.skills:
                        bool1 = True
                        break

                if player.__class__.__name__ == "Drummer":

                    if "play the drums with drumsticks" not in player.skills:
                        bool1 = True
                        break


        elif concert.genre == "Jazz":

            for player in band.members:

                if player.__class__.__name__ == "Singer":

                    if "sing high pitch notes" not in player.skills or "sing low pitch notes" not in player.skills:
                        bool1 = True
                        break

                if player.__class__.__name__ == "Guitarist":

                    if "play jazz" not in player.skills:
                        bool1 = True
                        break

                if player.__class__.__name__ == "Drummer":

                    if "play the drums with drum brushes" not in player.skills:
                        bool1 = True
                        break

        if bool1:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")


        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

