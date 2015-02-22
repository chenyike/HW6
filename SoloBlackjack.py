#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck
from Cards import *

class BlackJack():
    'Solitaire game'
    def __init__(self):
        'initialize BlackJack class'

    def get_value(self,card):
        'Get the value of the card'
        
    def initial_display(self):
        'Display the inital state of the game'
        self.disposal = []
        self.table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        print table[0:5]
        print table[5:10]
        print ' ',table[10:13]
        print ' ',table[13:16]
        

    def make_a_move(self,card):
        'Allow user to make a move'
        #print the card
        print "The top card of the deck is", card
        choice = raw_input('Do you want to put it into tableau?(Y or N):')
        if choice in 'Yy':
            slot=raw_input('which slot do you want to put it in: ')
        else:
            disposal.append(card)

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
        # initial display
        BlackJack.initial_display()

        # shuffle deck
        Deck.shuffle()
        
        # deal a card
        card = Deck.deal()
        
        # allow user to make a move
        BlackJack.make_a_move(card)
        
        # display current state of the game
        
        # repeat above 3 steps (deal card, place card, display game)
        
        # print a msg saying I am about to score the hand, pass table to score function

        # final msg to display the score of table
        
        # highest score display if user breaks the record
        
        # restart choice
        
        #.........................................



def main():
    bj_solitaire = BlackJack()
    # display the initial state of the game
    bj.solitaire.play()

    

if __name__ =="__main__":
    main()
