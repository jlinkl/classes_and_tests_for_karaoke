class Room:
    def __init__(self, capacity, entry_fee):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []
        self.tab = 0

    def get_capacity(self):
        return self.capacity
    
    def get_entry_fee(self):
        return self.entry_fee

    def get_songs(self):
        return self.songs

    def get_guests(self):
        return self.guests

    def add_guest_to_list(self, guest):
        if self.can_guest_checkin() and self.can_afford_entry_fee(guest):
            self.guests.append(guest)
            self.tab += self.entry_fee

    def remove_guest_from_list(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song_to_list(self, song):
        self.songs.append(song)

    def can_guest_checkin(self):
        if len(self.guests) + 1 > self.capacity:
            return False
        else:
            return True
    
    def can_afford_entry_fee(self, guest):
        if self.entry_fee < guest.wallet:
            return True
        else:
            return False

    # def add_new_guest_to_room(self, guest):
    #     if self.can_guest_checkin() and self.can_afford_entry_fee(guest):
    #         self.guests.append(guest)

    def find_fav_song(self, guest):
        for song in self.songs:
            if guest.fav_song == song.track:
                return "Woo"

    def sell_drink(self, bar, guest):
        if guest.wallet >= (bar.price + self.tab):
            self.tab += bar.price
    