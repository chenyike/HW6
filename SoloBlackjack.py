#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck
from Cards import *

class BlackJack():
    'Solitaire game'
    def __init__(self):
        'initialize BlackJack class'
        self.disposal = []
        self.table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def get_value(self,card):
        'Get the value of the card'
        print card.rank
        
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
            self.table[slot-1]= str(card)
        else:
            self.disposal.append(card)

    def current_display(self):
        'Display the current state of the game'
        print 'The new table looks like this: \n'
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]

    def score_hand(self,hand):
        'About to score the hands'
        self.Sum=0
        for i in hand:
            self.Sum += int(i[0])
        if self.Sum<=10:
            for i in hand:
                if '1'== i(1):
                    self.Sum += 10
        if self.Sum<=16:
            return 1
        if self.Sum==17:
            return 2
        if self.Sum==18:
            return 3
        if self.Sum==19:
            return 4
        if self.Sum==20:
            return 5
        if self.Sum==21:
            return 7
        
            
    def score_table(self):
        'Score the entire table by calling score hand nine times'
        self.score=0
        self.hand1=self.table[0:5]
        self.hand2=self.table[5:10]
        self.hand3=self.table[10:13]
        self.hand4=self.table[13:16]
        self.hand5=[self.table[0],self.table[5]]
        self.hand6=[self.table[4],self.table[9]]
        self.hand7=[self.table[1],self.table[6],self.table[10],self.table[13]]
        self.hand8=[self.table[2],self.table[7],self.table[11],self.table[14]]
        self.hand9=[self.table[3],self.table[8],self.table[12],self.table[15]]
        hands=[self.hand1,self.hand2,self.hand3,self.hand4,self.hand5,self.hand7,self.hand8,self.hand9]
        for i in hands:
            self.score += self.score_hand(i)
        return self.score

    def final_display(self):
        'display the score of table'
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]

    def highest_score(self):
        'If the current score is the highest so far, print a nice congrats msg'

    def restart(self):
        'Choice to restart the game'
    
    def play(self):
        'Play Solitaire Game'
        # initial display
        self.initial_display()

        # shuffle deck
        deck = Deck()
        deck.shuffle()
        
        
        # repeat above 3 steps (deal card, place card, display game)
        while len(deck.get_deck())+len(self.disposal)>36:
            # deal a card
            card = deck.deal()
            # allow user to make a move
            self.make_a_move(card)
            # display current state of the game
            self.current_display()
            
        self.final_display()
        score=self.score_table()
        print score
        
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
