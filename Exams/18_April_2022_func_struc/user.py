class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned  = []


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):

        if value == "":
            raise ValueError("Invalid username!")

        self.__username = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):


        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value


    def __str__(self): ## if error check
        list = []
        list.append(f"Username: {self.username}, Age: {self.age}")
        list.append("Liked movies:")
        if not self.movies_liked:
            list.append("No movies liked.")
        else:
            for thng in self.movies_liked:
                list.append(thng.details())

        list.append("Owned movies:")
        if not self.movies_owned:
            list.append("No movies owned.")
        else:
            for thing in self.movies_owned:
                list.append(thing.details())

        return "\n".join(list)
