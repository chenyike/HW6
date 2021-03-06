#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck

class Card(object):
    'Create a class containg the information of the card'
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank 
    
    def __init__(self, r, s):
        '' 'Initial the class'''
        #implement
        #where r is the rank, s is suit
        self.rank = r
        self.suit = s


    def __str__(self):
        '''Output the string'''
        return str(self.rank) + str(self.suit)


    def get_rank(self):
        '''output rank'''
        return self.rank.upper()


    def get_suit(self):
        '''Get suit'''
        return self.suit.upper()


class Deck():
    """Denote a deck to play cards with"""
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        self.__deck = []
        for rank in range(2,11):
            for suit in ['H','C','D','S']:
                card = Card(rank, suit)
                self.__deck.append(card)
        for rank in ['J', 'Q', 'K', 'A']:
            for suit in ['H', 'C' , 'D' , 'S']:
                card = Card(rank, suit)
                self.__deck.append(card)


    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)


    def get_deck(self):
        '''Get deck'''
        return self.__deck


    def deal(self):
        '''Deal the last card in the deck'''
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        deal_card = self.__deck[-1]
        
        self.__deck.pop()
        return deal_card

            
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        output_string = ''
        output_string += 'deck is listed below: \n'
        length = len(self.__deck)
        for card in self.__deck:
            output_string += str(card.rank) +card.suit + '\t'
        return output_string


