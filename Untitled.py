#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck
from Cards import *

class BlackJack():
    'Solitaire game'
    def __init__(self):
        'initialize BlackJack class'
        self.disposal = []
        self.table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def get_value(self,rank):
        'Get the value of the card'
        if rank in 'KJQ':
            return 10
        elif rank == 'A':
            return 1
        
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
        if choice == 'Y' or choice=='y':
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
        for i in range(0,len(hand)):
            #print hand[i][0]
            if len(hand[i])==2:
                self.Sum += int(hand[i][0])
            elif len(hand[i])==3:
                self.Sum += int(hand[i][0]+hand[i][1])
        if self.Sum<=10:
            for i in range(0,len(hand)):
                if len(hand[i])==2 and '1'== hand[i][0]:
                    self.Sum += 10
                if self.Sum>10:
                    break
                
        if self.Sum<=16:
            return 1
        elif self.Sum==17:
            return 2
        elif self.Sum==18:
            return 3
        elif self.Sum==19:
            return 4
        elif self.Sum==20:
            return 5
        elif self.Sum==21:
            return 7
        else:
            return 0
        
            
    def score_table(self):
        'Score the entire table by calling score hand nine times'
        for i in range(0,16):
            rank = self.table[i][0]
            suit = self.table[i][1]
            if rank in 'JQKA':
                self.table[i] = str(self.get_value(rank))+ suit
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]
            
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
        hands=[self.hand1,self.hand2,self.hand3,self.hand4,self.hand5,self.hand6,self.hand7,self.hand8,self.hand9]
        for i in range(0,9):
            self.score += self.score_hand(hands[i])
        return self.score

    def final_display(self):
        'display the score of table'
        print self.table[0:5]
        print self.table[5:10]
        print ' ',self.table[10:13]
        print ' ',self.table[13:16]

    def highest_score(self,score):
        'If the current score is the highest so far, print a nice congrats msg'
        #Show them ways to write from a file.
        fo = open('highScore.txt', 'r+')
        scores=[]
        for line in fo:
            scores.append(line)
        count=0
        for i in range(0, len(scores)):
            if score <= scores[i]:
                count += 1
        if count==0:
            print 'Congratulation! You just break the record!'
        num = str(score)+'\n'
        fo.write(num)
        fo.close
        
        
    def restart(self):
        'Choice to restart the game'
        self.restart = raw_input("Do you want to restart?(Y or N)? ")
        if self.restart == "Y" or self.restart == 'y':
            self.__init__()
            self.play()
    
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
        
        # print a msg saying I am about to score the hand, pass table to score function
        print "Congratulation! You finished the game!"
        score=self.score_table()
        print 'Your score is ', score, '\n'
        
        # highest score display if user breaks the record
##        self.highest_score(score)
           
        # restart choice
        self.restart()
        
        #.........................................



def main():
    bj_solitaire = BlackJack()
    bj_solitaire.play()

    

if __name__ =="__main__":
    main()
