class Player:

  def __init__(self, name, hp, mp):
    self.name = name
    self.hp = hp
    self.mp = mp
    self.skills = {}
    self.guild = "Unaffiliated"


  def add_skill(self, skill_name, mana_cost):

    if skill_name in self.skills.keys():
      return "Skill already added"

    self.skills[skill_name] = mana_cost
    return f"Skill {skill_name} added to the collection of the player {self.name}"


  def player_info(self):
    to_return = []

    to_return.append(f"Name: {self.name}")
    to_return.append(f"Guild: {self.guild}")
    to_return.append(f"HP: {self.hp}")
    to_return.append(f"MP: {self.mp}")

    for key,value in self.skills.items():
      to_return.append(f"==={key} - {value}")

    return "\n".join(to_return)
    