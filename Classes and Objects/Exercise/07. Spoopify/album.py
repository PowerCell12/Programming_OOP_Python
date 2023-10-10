from project.song import Song

class Album:

    def __init__(self, name, *song):
        self.name = name
        self.song = song
        self.published = False
        self.songs =  []


    def add_song(self, song: Song):

        if song.single == True:
            return f"Cannot add {song.name}. It's a single"
        
        if self.published == True:
            return "Cannot add songs. Album is published."
        
        if song in self.songs:
            return "Song is already in the album."
        
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."
    

    def remove_song(self, song_name):

        for song in self.songs:

            if song.name == song_name:

                if self.published == True:
                    return "Cannot remove songs. Album is published."
                
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            
        return "Song is not in the album."
    


    def publish(self):

        if self.published == True:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."
    

    def details(self):
        to_return = []

        to_return.append(f"Album {self.name}")
        
        for song1 in self.songs:

            to_return.append(f"== {song1.get_info()}")

        return "\n".join(to_return)
