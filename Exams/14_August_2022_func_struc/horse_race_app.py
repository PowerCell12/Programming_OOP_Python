from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses =[]
        self.jockeys =[]
        self.horse_races =[]


    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type != "Appaloosa" and horse_type != "Thoroughbred":
            pass
        else:
            if horse_type == "Appaloosa":
                self.horses.append(Appaloosa(horse_name, horse_speed))
            else:
                self.horses.append(Thoroughbred(horse_name, horse_speed))

            return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):

        bool1 = False

        for jockey in self.jockeys:

            if jockey.name == jockey_name:
                bool1= True
                break

        if bool1:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            self.jockeys.append(Jockey(jockey_name, age))

            return f"Jockey {jockey_name} is added."


    def create_horse_race(self, race_type: str):

        bool1  = False

        for race in self.horse_races:

            if race.race_type == race_type:
                bool1 = True
                break
        if bool1:
            raise Exception(f"Race {race_type} has been already created!")
        else:
            self.horse_races.append(HorseRace(race_type))

            return f"Race {race_type} is created."



    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        is_jockey = False

        for jockey in self.jockeys:

            if jockey.name == jockey_name:
                is_jockey = True
                break

        if not is_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")


        if_horse = False

        for horse in self.horses:

            if horse.__class__.__name__ == horse_type and horse.is_taken == False:
                if_horse = True
                break
        if not if_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")


        for jockey in self.jockeys:

            if jockey.name == jockey_name:
                if jockey.horse != None:
                    return f"Jockey {jockey_name} already has a horse."

        horse = None

        for i in range(len(self.horses) - 1, -1, -1):

            if self.horses[i].__class__.__name__ == horse_type and self.horses[i].is_taken == False:

                self.horses[i].is_taken = True
                for jokecy in self.jockeys:

                    if jokecy.name == jockey_name:
                        jokecy.horse = self.horses[i]
                        return f"Jockey {jockey_name} will ride the horse {self.horses[i].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        if_type_exists = False

        for race in self.horse_races:

            if race.race_type == race_type:
                if_type_exists = True
                break

        if not if_type_exists:
            raise Exception(f"Race {race_type} could not be found!")


        if_jockey  = False

        for jockey in self.jockeys:

            if jockey.name == jockey_name:
                if_jockey = True
                break

        if not if_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")


        for jockey in self.jockeys:

            if jockey.name == jockey_name:

                if jockey.horse == None:
                    raise Exception(f"Jockey {jockey_name} cannot race without a horse!")


        for race in self.horse_races:
            if race.race_type == race_type:

                for thing in race.jockeys:

                    if thing.name == jockey_name:
                        return f"Jockey {jockey_name} has been already added to the {race_type} race."

        for race in self.horse_races:
            if race.race_type == race_type:
                for jockey in self.jockeys:
                    if jockey.name == jockey_name:
                        race.jockeys.append(jockey)
                        return f"Jockey {jockey_name} added to the {race_type} race."



    def start_horse_race(self,race_type: str):

        bool1 = False

        for race in self.horse_races:

            if race.race_type == race_type:
                bool1 = True
                break

        if not bool1:
            raise Exception(f"Race {race_type} could not be found!")


        for race in self.horse_races:

            if race.race_type == race_type:

                if len(race.jockeys)  < 2:
                    raise Exception(f"Horse race {race_type} needs at least two participants!")


        fasteet_jockey = None

        for race in self.horse_races:

            if race.race_type == race_type:

                for i in range(len(race.jockeys)):
                    jockey = race.jockeys[i]

                    if i == 0:
                        fasteet_jockey = jockey
                    else:
                        if jockey.horse.speed > fasteet_jockey.horse.speed:
                            fasteet_jockey = jockey

        return f"The winner of the {race_type} race, with a speed of {fasteet_jockey.horse.speed}km/h is {fasteet_jockey.name}! Winner's horse: {fasteet_jockey.horse.name}."
