class Music_library():

    def __init__(self):
        self.library = {}

    def add_track(self, artist, title):
        if isinstance(artist, str) and isinstance(title, str):
            if artist.strip() == "" or title.strip() =="":
                raise Exception("Please provide track details")
            if artist not in self.library and title not in self.library.values():
                self.library[artist] = title
            else: 
                raise Exception("Track already exists")
        else:
            raise TypeError("Please enter text")

    def view_library(self):
        if self.library == {}:
            raise Exception("Library is empty")
        else:
            return self.library