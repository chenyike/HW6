#author - Yike Chen and Yejia Li

import unittest
from cards import *


class Test_cards(unittest.TestCase):

    def setUp(self):
        self.card = Card('A','S')
        self.card2 = Card('2','d')


    def test_init(self):
        self.assertEqual(self.card.rank,'A')
        self.assertEqual(self.card.suit,'S')

        
    def test_get_rank(self):
        rank = Card.get_rank(self.card)
        self.assertEqual(rank,'A')
        # check if the
        rank2 = Card.get_rank(self.card2)
        self.assertEqual(rank2,'2')

        
    def test_get_suit(self):
        suit = Card.get_suit (self.card)
        self.assertEqual(suit,'S')
        # test if it applied to lower case suit
        suit2 = Card.get_suit (self.card2)
        self.assertEqual(suit2,'D')


class Test_Deck(unittest.TestCase):
    def setUp(self):
        self.card = Card('A','S')
        self.deck = Deck()

        
    def test_init(self):
        get_deck = self.deck.get_deck()
        #test length 
        self.assertEqual(len(get_deck),52)
        output = ''
        for card in get_deck:
            output += str(card.rank) +card.suit
        #test random cards
        self.assertTrue(self.card.rank+self.card.suit in output)
        self.assertTrue('10C' in output)
        self.assertTrue('6D' in output)
        self.assertTrue('KS' in output)


    def test_shuffle(self):
        # get the initial string of the deck
        initial_deck = self.deck.get_deck()
        output_initial = ''
        for card in initial_deck:
            output_initial += str(card.rank) +card.suit
        # get the shuffled string of the deck
        self.deck.shuffle()
        shuffled_deck = self.deck.get_deck()
        output_shuffled = ''
        for card in shuffled_deck:
            output_shuffled += str(card.rank) +card.suit           
        #test length 
        self.assertEqual(len(shuffled_deck),52)
        # test if anything changes after shuffle
        self.assertFalse(output_initial == output_shuffled)


    def test_deal(self):
        # get the last card from the pile
        get_deck = self.deck.get_deck()
        (rank,suit) = (get_deck[-1].rank,get_deck[-1].suit)
        before_deal = len(get_deck)
        deal_card = self.deck.deal()
        (rank2,suit2) = (deal_card.rank,deal_card.suit)
        after_deal = len(get_deck)
        self.assertEqual(before_deal,after_deal+1)
        self.assertEqual((rank,suit),(rank2,suit2))


        
unittest.main()
