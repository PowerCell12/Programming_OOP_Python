from math import ceil


class PhotoAlbum:

    def __init__(self,  pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
## every list has a length of 4 no more !!!


    @classmethod
    def from_photos_count(cls, photo_count):

        return cls(ceil(photo_count / 4))


    def add_photo(self, label):

        for i in range(len(self.photos)):
            photo = self.photos[i]
            if len(photo) < 4:
                photo.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {photo.index(label) + 1}"
            
        return "No more free slots"
    

    def display(self):
        to_return = []

        for page in self.photos:
            to_return.append("-" * 11)

            string = ""
            for i in range(len(page)):
                if i == len(page) - 1:
                    string += "[]"
                else: string += "[] "


            to_return.append(string)   

        to_return.append("-" * 11)
        return "\n".join(to_return)
    

