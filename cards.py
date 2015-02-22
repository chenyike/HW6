#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck

class Card(object):
    'Create a class containg the information of the card'
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank 
    
    def __init__(self, r, s):
        'Initial the class'
        self.rank = r
        self.suit = s 

    def __str__(self):

        'Output the string'
        return 'this is '+ str(self.rank) + str(self.suit.upper())
    
    def get_rank(self):
        'Get rank'
        if self.rank == 'K' or self.rank == 'k':
            return 10
        elif self.rank == 'Q' or self.rank == 'q':
            return 12
        elif self.rank == 'J' or self.rank == 'j':
            return 11
        elif self.rank == 'A' or self.rank == 'a':
            return 1
        return self.rank

    def get_suit(self):
        'Get suit'
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
        'Get deck'
        return self.__deck

    def deal(self):
        'Deal the last card in the deck'
        # get the last card in the deck
        # simulates a pile of cards and getting the top one

        return self.__deck.pop             ###
        ###raise NotImplementedError   
        #  return self.__deck[-1]          ###

##            
##    def __str__(self):
##        """Represent the whole deck as a string for printing -- very useful during code development"""
##      
##       #the deck is a list of cards
##       #this function just calls str(card) for each card in list
##       # put a '\n' between them




    
def main():
    Solitaire()
    deck=Deck()
    deck.shuffle()
##    x = deck.get_deck()
##    output_string = ''
##    output_string += 'deck is listed below: \n'
##    length=len(x)
##    for card in x:
##        output_string += str(card.rank) +card.suit +'\t'
##    print output_string 
    


if __name__ =="__main__":
    main()
>>>>>>> Stashed changes
