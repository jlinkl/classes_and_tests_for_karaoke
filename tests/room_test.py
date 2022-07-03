import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(8, 5)
        self.room1 = Room(1, 5)
        self.room2 = Room(5, 200)

        self.guest = Guest("James", "Legend", 100)
        self.guest1 = Guest("Ifti", "Radioactive", 150)
        self.guest2 = Guest("Ben", "Techno Kitty", 100)

        self.song = Song("Legend", "Tevvez")

        self.bar = Bar("Coke", 3)
        self.bar1 = Bar("Tennents", 5)
        
    def test_room_capacity(self):
        self.assertEqual(8, self.room.get_capacity())

    def test_room_entry_fee(self):
        self.assertEqual(5, self.room.get_entry_fee())

    def test_room_songs(self):
        self.assertEqual([], self.room.get_songs())

    def test_add_guest_to_list(self):
        self.room.add_guest_to_list(self.guest)
        self.assertEqual([self.guest], self.room.get_guests())

    def test_remove_guest_from_list(self):
        self.room.add_guest_to_list(self.guest)
        self.room.add_guest_to_list(self.guest1)
        self.assertEqual([self.guest, self.guest1], self.room.get_guests())
        self.room.remove_guest_from_list(self.guest)
        self.assertEqual([self.guest1], self.room.get_guests())

    def test_add_song_to_list(self):
        self.room.add_song_to_list(self.song)
        self.assertEqual([self.song], self.room.get_songs())

    def test_guest_checkin_false(self):
        self.room1.add_guest_to_list(self.guest)
        self.room1.add_guest_to_list(self.guest1)
        self.assertEqual(False, self.room1.can_guest_checkin())

    def test_can_afford_entry_fee_false(self):
        self.assertEqual(False, self.room2.can_afford_entry_fee(self.guest))

    def test_can_afford_entry_fee_true(self):
        self.assertEqual(True, self.room.can_afford_entry_fee(self.guest))

    def test_guest_checkin_true(self):
        self.room.add_guest_to_list(self.guest)
        self.room.add_guest_to_list(self.guest1)
        self.assertEqual(True, self.room.can_guest_checkin())

    def test_find_fav_song(self):
        self.room.add_song_to_list(self.song)
        self.room.add_guest_to_list(self.guest)
        self.assertEqual("Woo", self.room.find_fav_song(self.guest))

    def test_sell_drink(self):
        self.room.sell_drink(self.bar, self.guest)
        self.assertEqual(3, self.room.tab)

    def test_calculate_tab(self):
        self.room.add_guest_to_list(self.guest)
        self.room.add_guest_to_list(self.guest1)
        self.room.sell_drink(self.bar,self.guest)
        self.assertEqual(13, self.room.tab)