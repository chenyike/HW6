#author - Yike Chen and Yejia Li

import unittest
from SoloBlackjack import *
from Cards import *


class Test_BlackJack(unittest.TestCase):

    def setUp(self):
        self.bj = BlackJack()
        self.card = Card('A','S')
        self.choice = 'N'
        self.disposal = BlackJack.initial_display().disposal


    # No need to test a function which does nothing but print out stuff
    def test_initial_display(self):
        self.bj.initial_display()

    def test_make_a_move(self):
        self.bj.make_a_move(self.card)
        self.assertEqual(self.disposal[-1],self.card)
    
    
        
unittest.main()
