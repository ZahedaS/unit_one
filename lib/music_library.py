class Music_library():

    def __init__(self):
        self.library = {}

    def add_track(self, artist, title):
        self.library[artist] = title

    def view_library(self):
        if self.library == {}:
            raise Exception("Library is empty")
        else:
            return self.library