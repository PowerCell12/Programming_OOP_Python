from project.room import Room


class Hotel:


  def __init__(self, name):
    self.name = name
    self.rooms = []
    self.guests = 0


  @classmethod
  def from_stars(cls, stars):
    return cls(f"{stars} stars Hotel")


  def add_room(self, room: Room):
    self.rooms.append(room)



  def take_room(self, room_number, people):

    for room in self.rooms:

      if room.number == room_number:

        if people > room.capacity:
          return None
        else:
            room.is_taken = True
            room.guests = people
            self.guests += people
            

    return None


  def free_room(self, room_number):

    for room in self.rooms:

      if room.number == room_number:
        to_get = room.guests
        
        room.is_taken = False
        room.guests = 0
        self.guests -= to_get

    return None



  def status(self):
    to_return = []

    to_return.append(f"Hotel {self.name} has {self.guests} total guests")

    free_rooms = []
    taken_rooms = []

    for i in range(len(self.rooms)):
      room = self.rooms[i]

      if room.is_taken == False:
        free_rooms.append(str(i + 1))
      else:
        taken_rooms.append(str(i + 1))


    to_return.append(f"Free rooms: {', '.join(free_rooms)}")
    to_return.append(f"Taken rooms: {', '.join(taken_rooms)}")

    return '\n'.join(to_return)


## done just resend it 