import unittest
from Source.Tool.linguifiy_class import Linguify

class TestLinguify(unittest.TestCase):

    def setUp(self):
        """Initialize a Linguify instance before each test"""
        self.linguify = Linguify()

    def test_instance_ID_getter_setter(self):
        """Test getter and setter for instance_ID"""
        self.linguify.instance_ID = 123
        self.assertEqual(self.linguify.instance_ID, 123)
        
        with self.assertRaises(TypeError):
            self.linguify.instance_ID = "string_id"
    
        with self.assertRaises(ValueError):
            self.linguify.instance_ID = -1

    def test_file_name_getter_setter(self):
        """Test getter and setter for file_name"""
        self.linguify.file_name = "playlist.txt"
        self.assertEqual(self.linguify.file_name, "playlist.txt")
        
        with self.assertRaises(TypeError):
            self.linguify.file_name = 1234

    def test_num_of_playlists_getter_setter(self):
        """Test getter and setter for num_of_playlists"""
        self.linguify.num_of_playlists = 5
        self.assertEqual(self.linguify.num_of_playlists, 5)
        
        with self.assertRaises(TypeError):
            self.linguify.num_of_playlists = "five"
        
        with self.assertRaises(ValueError):
            self.linguify.num_of_playlists = -1

    def test_set_playlists(self):
        """Test the set_playlists method"""
        self.linguify.num_of_playlists = 3
        valid_playlists = ["playlist1", "playlist2", "playlist3"]
        self.linguify.set_playlists(valid_playlists)
        self.assertEqual(self.linguify.playlists, valid_playlists)
        
        with self.assertRaises(ValueError):
            self.linguify.set_playlists(["playlist1", "playlist2"])

    def test_extractArtistData(self):
        """Test the extractArtistData method (assuming you implement this later)"""
        self.assertIsNone(self.linguify.extractArtistData())

if __name__ == "__main__":
    unittest.main()