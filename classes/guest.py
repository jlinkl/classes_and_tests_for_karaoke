
class Guest:
    def __init__(self, name, fav_song, wallet):
        self.name = name
        self.fav_song = fav_song
        self.wallet = wallet

    def get_name(self):
        return self.name
    
    def get_fav_song(self):
        return self.fav_song
    
    def get_wallet(self):
        return self.wallet


