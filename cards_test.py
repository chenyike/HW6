#author - Yike Chen and Yejia Li

import unittest
from cards import *


class Test_cards(unittest.TestCase):

    def setUp(self):
        self.card = Card(1,'S')
        self.deck = Deck()

    def test_init(self):
        self.assertEqual(self.card.rank,'1')
        self.assertEqual(self.card.suit,'S')
        
    def test_get_rank(self):
        rank = Card.get_rank(self.card)
        self.assertEqual(rank,'1')
        
    def test_get_suit(self):
        suit = Card.get_suit (self.card)
        self.assertEqual(suit,'S')

    def test_init(self):
        length = len(self.deck.__deck)
        self.assertEqual(length, 52)

    

        
unittest.main()
