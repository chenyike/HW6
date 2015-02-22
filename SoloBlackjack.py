#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck
from cards import *


class BlackJack():
    'Solitaire game'
    def __init__(self):
        'initialize BlackJack class'
        self.disposal = []
        self.table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def get_value(self,card):
        'Get the value of the card'
        
    def initial_display(self):
        'Display the inital state of the game' 

        print 'The table looks like this, also, numbers on it mark the slots: \n',
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]


    def make_a_move(self,card):
        'Allow user to make a move'
        #print the card
        print "The top card of the deck is", str(card.rank) +card.suit
        choice = raw_input('Do you want to put it into the table?(Y or N): ')
        if choice in 'Y' or 'y':
            slot=input('which slot do you want to put it in: ')
            self.table[slot-1]=str(card)
        else:
            self.disposal.append(card)

    def current_display(self):
        'Display the current state of the game'
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]

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
        # initial display
        self.initial_display()

        # shuffle deck

        Deck().shuffle()
        
        # deal a card
        while len(Deck().get_deck())+len(self.disposal)>36:
            card = Deck().deal()
            self.make_a_move(card)
            self.current_display()
        
        # display current state of the game
        
        # repeat above 3 steps (deal card, place card, display game)
        
        # print a msg saying I am about to score the hand, pass table to score function

        # final msg to display the score of table
        
        # highest score display if user breaks the record
        
        # restart choice
        
        #.........................................



def main():
    bj_solitaire = BlackJack()
    bj_solitaire.play()

    

if __name__ =="__main__":
    main()
