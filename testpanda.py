import sys
import unittest
from panda import Panda


class TestPanda(unittest.TestCase):

    #def setUp(self):
    #    self.p = Panda("k", 15)

    def test_panda_is_instance_of_panda(self):
        p = Panda("k", 15) 
        # si on change on met 10 au lieu du nom il affiche erreur faut etre alphabetique
        self.assertIsInstance(p, Panda)
        #self.assertIsInstance(self.p, Panda)

    def test_panda_age_is(self):
        p = Panda("k", 15) 
        self.assertGreater(p.age, 0)
        #self.assertGreater(self.p.age, 0)



if __name__ == "__main__":
    unittest.main()