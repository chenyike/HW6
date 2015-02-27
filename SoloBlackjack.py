#author - Yike Chen and Yejia Li

import random  # needed for shuffling a Deck
from cards import *

class BlackJack():
    '''Solitaire game'''
    def __init__(self):
        '''initialize BlackJack class'''
        self.disposal = []
        self.table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##        self.slot = -1
##        self.choice = ''

        
    def get_value(self,rank):
        '''Get the value of the card'''
        if rank in 'KJQ':
            return 10
        elif rank == 'A':
            return 1

        
    def initial_display(self):
        '''Display the inital state of the game'''
        print 'The table looks like this, also, numbers on it mark the slots: \n',
        row1= ''
        row2= ''
        row3= ''
        row4= ''
        print 'The new table looks like this: '
        for card in self.table[0:5]:
            row1 += str(card)+ '\t '
        print row1
        for card in self.table[5:10]:
            row2 += str(card)+ ' \t'
        print row2
        for card in self.table[10:13]:
            row3 += str(card)+ ' \t'
        print '\t', row3
        for card in self.table[13:16]:
            row4 += str(card)+ ' \t'
        print '\t', row4, '\n'


    def user_input(self,card):
        '''Deal with user input'''
        #print the card
        print "The top card of the deck is", str(card.rank) +card.suit
        choice = raw_input('Do you want to put it into the table?(Y or N): ')
        while choice not in 'YyNn':
            choice = raw_input('Do you want to put it into the table?(Y or N): ')
        if self.isDisposalFull():
            while choice in 'Nn':
                print 'Sorry, the disposal area is fully occupied. You have to put the card onto the table'
                choice = raw_input('Do you want to put it into the table?(Y or N): ')
                while choice not in 'YyNn':
                    choice = raw_input('Do you want to put it into the table?(Y or N): ')
        if choice in 'Yy':
            slot = raw_input('which slot do you want to put it in: ')
        elif choice in 'Nn':
            slot = '-1'
        print
        return (choice,slot)


    def isDisposalFull(self):
        '''Judge to see if disposal is full'''
        n=0
        if len(self.disposal)>3:
            n+=1
        if n>0:
            return True
        else:
            return False


    def error_checking(self,card,choice,slot):
        '''Check input'''
        if choice in 'Nn':
            return (choice,slot)
        elif choice in 'Yy':
            while(True):
                n=0
                # check if the input is number or not
                for letter in slot:
                    if letter not in '1234567890':
                        n += 1
                if  n>0:
                    print 'Error input, not a number!\n'
                    (choice,slot) = self.user_input(card)
                # check if the number is out of range
                elif int(slot) <1 or int(slot) >16:
                    print 'Error input, out of range!\n'
                    (choice,slot) = self.user_input(card)
                # if the number is in range, put it in the table
                elif type(self.table[int(slot)-1]) != int:
                    print 'Error input, seat occupied!\n'
                    (choice,slot) = self.user_input(card)
                else:
                    break
        return (choice,slot)

            
    def make_a_move(self,card,choice,slot):
        '''Allow user to make a move'''
        if choice in 'Yy' and int(slot)>0:
            self.table[int(slot)-1]= card
        elif choice in 'Nn':
            self.disposal.append(card)


    def current_display(self):
        '''Display the current state of the game'''
        row1= ''
        row2= ''
        row3= ''
        row4= ''
        print 'The new table looks like this: '
        for card in self.table[0:5]:
            row1 += str(card)+ '\t '
        print row1
        for card in self.table[5:10]:
            row2 += str(card)+ ' \t'
        print row2
        for card in self.table[10:13]:
            row3 += str(card)+ ' \t'
        print '\t', row3
        for card in self.table[13:16]:
            row4 += str(card)+ ' \t'
        print '\t', row4, '\n'

        print 'The disposal deck looks like this: '
        for card in self.disposal:
            print str(card)
        print


    def BlackJack(self,hand):
        '''Check if blackjack has been reached'''
        n=0
        if len(hand)==2:
            if ('10' in hand[0] and '1' in hand[1] and len(hand[1])==2) or ( '10' in hand[1] and '1' in hand[0] and len(hand[1])==3):
                n +=1
        if n>0:
            return True
        else:
            return False
                
        
    def score_hand(self,hand):
        '''About to score the hands'''
        #score the hand and sum up.
        self.Sum=0
        for i in range(0,len(hand)):
            if len(hand[i])==2:
                self.Sum += int(hand[i][0])
            elif len(hand[i])==3:
                self.Sum += int(hand[i][0]+hand[i][1])               
        #check if Ace exist and find the optimal score mothod
        if self.Sum<=11:
            for i in range(0,len(hand)):
                if len(hand[i])==2 and '1'== hand[i][0]:
                    self.Sum += 10
                if self.Sum>11:
                    break
        #return the score of the hand of card.
        if not self.BlackJack(hand):
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
        elif self.BlackJack(hand):
            return 10
        
            
    def score_table(self):
        '''Score the entire table by calling score hand nine times'''
        for i in range(0,16):
            self.table[i]=str(self.table[i])       
        #get value of cards whose rank is among 'JQKA'          
        for i in range(0,16):
            rank = self.table[i][0]
            suit = self.table[i][1]
            if rank in 'JQKA':
                self.table[i] = str(self.get_value(rank))+ suit
        #9 hands of cards
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
        '''display the score of table'''
        print "Congratulation! You finished the game!"
        print 'Your score is ', self.score_table()


    def write_score(self,filename, score):
        '''If the current score is the highest so far, print a nice congrats msg'''
        #Show them ways to write from a file.
        fo = open(filename,'a')
        eachline=str(score)+'\n'
        fo.write(eachline)
        fo.close


    def highest_score(self, score):
        '''Calculate the score out from the txt file'''
        scorelist = []
        fo = open('highScore.txt','r')
        for line in fo:
            if len(line)==2 or len(line)==1:
                scorelist.append(int(line[0]))
            else:
                scorelist.append(int(line[0]+line[1]))
        self.write_score('highScore.txt',score)
        if scorelist==[]:
            return False
        elif score >= max(scorelist) and max(scorelist)!=0:
            return True
        else:
            return False
        fo.close



    def restart(self):
        '''Choice to restart the game'''
        start= raw_input("Do you want to restart?(Y or N)? ")
        if start == "Y" or start == 'y':
            self.__init__()
            self.play()


    def play(self):
        '''Play Solitaire Game'''
        HighestScore=0
        # initial display
        self.initial_display()
        # shuffle deck
        deck = Deck()
        #print deck
        deck.shuffle()
        
        # repeat above 3 steps (deal card, place card, display game)
        while len(deck.get_deck())+len(self.disposal)>36:
            # deal a card
            card = deck.deal()
            # user input
            (choice,slot) = self.user_input(card)
            # Error_checking
            (choice,slot) = self.error_checking(card,choice,slot)
            # allow user to make a move
            self.make_a_move(card,choice,slot)
            # display current state of the game
            self.current_display()
            
        self.final_display()
        
        # highest score display if user breaks the record
        if self.highest_score(self.score_table()):
             print 'Congratulation! You just break the record!'
        
        # restart choice
        self.restart()


def main():
    '''main function'''
    bj_solitaire = BlackJack()
    bj_solitaire.play()

    

if __name__ =="__main__":
    main()
