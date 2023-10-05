from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.dict = {}

    def add_pokemon(self, pokemon: Pokemon):

        if pokemon.name not in self.pokemons:

            self.pokemons.append(pokemon.name)
            self.dict[pokemon.name] = pokemon.health
            return f"Caught {pokemon.name} with health {pokemon.health}"
        
        return "This pokemon is already caught"
    
    def release_pokemon(self, pokemon_name):

        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            del self.dict[pokemon_name]
            return f"You have released {pokemon_name}"
        
        return "Pokemon is not caught"
    
    def trainer_data(self):

        string = ""
        string += f"Pokemon Trainer {self.name}\n"
        string += f"Pokemon count {len(self.pokemons)}\n"
        for key,value in self.dict.items():
            string += f"- {key} with health {value}\n"

        return string