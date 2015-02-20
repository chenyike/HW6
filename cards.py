import random  # needed for shuffling a Deck

class Card(object):
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank 
    
    def __init__(self, r, s):
        #implement
        #where r is the rank, s is suit
        return NotImplementedError

    def __str__(self):
        return 'this'

    def get_rank(self):
        return self.r

    def get_suit(self):
        return 0

class Deck():
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        #correct the code below
        self.__deck = []

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        raise NotImplementedError

    def deal(self):
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        raise NotImplementedError
    
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them 

