#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck

class Card(object):
    'Create a class containg the information of the card'
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank 
    
    def __init__(self, r, s):
        'Initial the class'
        #implement
        #where r is the rank, s is suit
        self.rank = str(r)
        self.suit = str(s)

    def __str__(self):
        'Output the string'
        return 'this is '+ str(self.rank) + str(self.suit)

    def get_rank(self):
        'Get rank'
        return self.rank

    def get_suit(self):
        'Get suit'
        return self.suit


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
        return self.__deck[-1]
            
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        output_string = ''
        output_string += 'deck is listed below: \n'
        length = len(self.__deck)
        for card in self.__deck:
            output_string += str(card.rank) +card.suit + '\n'
        return output_string


class BlackJack():
    'Solitaire game'
    def __init__(self):
        'initialize BlackJack class'

    
    def get_value(self,card):
        'Get the value of the card'
        
    def initial_display(self):
        'Display the inital state of the game'

    def make_a_move(self):
        'Allow user to make a move'

    def current_display(self):
        'Display the current state of the game'

    def score_hand(self):
        'About to score the hands'

    def score_table(self):
        'Score the entire table by calling score hand nine times'

    def final_display(self):
        'display the score of table'

    def highest_score(self):
        'If the current score is the highest so far, print a nice congrats msg'

    def restart(self):
        'Choice to restart the game'
    
    def play(self):
        'Play Solitaire Game'
        BlackJack.initial_display()
        BlackJack.make_a_move()



def main():
    bj_solitaire = BlackJack()
    # display the initial state of the game
    game.initial_display
    # shuffle deck
    # deal a card
    # allow user to make a move
    # display current state of the game
    # repeat above 3 steps (deal card, place card, display game)
    # print a msg saying I am about to score the hand, pass table to score function
    # final msg to display the score of table
    # highest score display if user breaks the record
    # restart choice
    

if __name__ =="__main__":
    main()
