import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("James", "Legend", 100)

    def test_guest_name(self):
        self.assertEqual("James", self.guest.get_name())

    def test_guest_fav_song(self):
        self.assertEqual("Legend", self.guest.get_fav_song())

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest.get_wallet())

    
