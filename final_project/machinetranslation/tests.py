import unittest

from translator import english_to_french, french_to_english

class TestMyProject(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french(""),"Error: Try again")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_fr_to_en(self):
        self.assertEqual(french_to_english(""),"Erreur : réessayez")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()