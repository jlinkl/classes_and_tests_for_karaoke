import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song ("Legend", "Tevvez")
    
    def test_get_track(self):
        self.assertEqual("Legend", self.song.get_track())

    def test_get_artist(self):
        self.assertEqual("Tevvez", self.song.get_artist())