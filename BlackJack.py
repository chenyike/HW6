#author - Yike Chen and Yejia Li

from cards import *

class Solitaire(object):

    def tableaus(self):
        self.disposal=[]
        self.tableau=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        
        
    def play(self):
        tableau=Solitaire.tableaus.tableau
        print tableau[0:5]
        print tableau[5:10]
        print ' ',tableau[10:13]
        print ' ',tableau[13:16]
        card=0
        print "The top card of the deck is", card
        take = raw_input('Do you want to put it into tableau?(Y or N):')
        if take=='Y'or 'y':
            slot=raw_input('which slot do you want to put it in: ')
        else:
            disposal.append(card)
     
def main():
    solitaire = Solitaire()
    solitaire.play()


if __name__ == '__main__':
    
    main()

 


