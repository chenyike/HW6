#author - Yike Chen and Yejia Li

import unittest
from SoloBlackjack import *
from cards import *


class Test_BlackJack(unittest.TestCase):

    def setUp(self):
        self.bj = BlackJack()
        self.bj.slot1 = 1
        self.bj.slot2 = 10
        self.bj.choice1 = 'Y'
        self.bj.choice2 = 'N'
        self.bj.card = Card('A','S')
        self.bj.card1 = 'AS'
        self.bj.card2 = '2d'
        self.bj.card3 = '4H'
        self.bj.card4 = '10S'
        self.bj.card5 = 'JD'
        self.bj.card6 = 'KS'
        self.bj.card7= 'AC'
        self.bj.card8 = '2S'
        self.bj.card9 = '4S'
        self.bj.card10 = '9S'
        self.bj.card11 = 'JS'
        self.bj.card12 = 'KD'
        self.bj.card13 = '4C'
        self.bj.card14 = '10C'
        self.bj.card15 = 'JC'
        self.bj.card16 = 'KC'
        

        self.bj.table = [self.bj.card1,self.bj.card2,self.bj.card3,self.bj.card4,self.bj.card5,\
                         self.bj.card6,self.bj.card7,self.bj.card8,self.bj.card9,self.bj.card10,\
                         self.bj.card11,self.bj.card12,self.bj.card13,self.bj.card14,self.bj.card15,self.bj.card16]
        self.bj.disposal = [1,2,3,4]


        
        
        self.bj.hand1 = ['4H', '6S']                                 #sum = 1
        self.bj.hand2 = ['7S', '1H', '9D', '1A']                 #sum = 3
        self.bj.hand3 = ['1S', '1H', '1D', '5A', '2H']         #sum = 5
        self.bj.hand4 = ['9S', '8A', '2D']                         #sum = 4
        self.bj.hand5 = ['10S', '10H', '9D', '5A']             #sum = 0
        self.bj.hand6 = ['1S', '1H', '1D', '1A', '3H']         #sum = 2
        self.bj.hand7 = ['1S', '1A', '1D']                         #sum = 1
        self.bj.hand8 = ['1S', '2H', '1D', '5A', '2H']         #sum = 7
        self.bj.hand9 = ['1H', '10S']                               #sum = 10


    def test_init(self):

        self.assertEqual(self.bj.disposal, [1,2,3,4])
        self.assertEqual(self.bj.table, ['AS', '2d', '4H', '10S', 'JD','KS','AC','2S','4S','9S','JS','KD','4C','10C','JC','KC'])       


    def test_get_value(self):
        self.assertEqual(self.bj.get_value(self.bj.card1[0]), 1)
        self.assertEqual(self.bj.get_value(self.bj.card5[0]), 10)
        self.assertEqual(self.bj.get_value(self.bj.card6[0]), 10)       
        

    def test_isDisposalFull(self):
        self.assertTrue(self.bj.isDisposalFull())


    def test_make_a_move(self):
        self.bj.table = [self.bj.card1,self.bj.card2,self.bj.card3,self.bj.card4,self.bj.card5,\
                         self.bj.card6,self.bj.card7,self.bj.card8,self.bj.card9,self.bj.card10,\
                         self.bj.card11,self.bj.card12,self.bj.card13,self.bj.card14,self.bj.card15,self.bj.card16]
        self.bj.disposal = []
        self.bj.make_a_move(self.bj.card,self.bj.choice2,self.bj.slot1)
        self.assertTrue(self.bj.card in self.bj.disposal)
        self.bj.make_a_move(self.bj.card,self.bj.choice1,self.bj.slot1)
        self.assertTrue(self.bj.card == self.bj.table[self.bj.slot1-1])


    def test_BlackJack(self):
        isBlackJack = self.bj.BlackJack(self.bj.hand9)
        self.assertTrue(isBlackJack)


    def test_score_hand(self):
        score1=self.bj.score_hand(self.bj.hand1)
        self.assertEqual(score1,1)
        
        score2=self.bj.score_hand(self.bj.hand2)
        self.assertEqual(score2,3)
        
        score3=self.bj.score_hand(self.bj.hand3)
        self.assertEqual(score3,5)
        
        score4=self.bj.score_hand(self.bj.hand4)
        self.assertEqual(score4,4)
        
        score5=self.bj.score_hand(self.bj.hand5)
        self.assertEqual(score5,0)
        
        score6=self.bj.score_hand(self.bj.hand6)
        self.assertEqual(score6,2)
        
        score7=self.bj.score_hand(self.bj.hand7)
        self.assertEqual(score7,1)

        score8=self.bj.score_hand(self.bj.hand8)
        self.assertEqual(score8,7)

        score9=self.bj.score_hand(self.bj.hand9)
        self.assertEqual(score9,10)

    def test_score_table(self):
        score = self.bj.score_table()
        self.assertEqual(score,14)
        

    def test_write_score(self):
        fo = open('highScore.txt','r+')
        self.bj.write_score('highScore.txt',6)       
        score=fo.read()
        self.assertTrue('6\n' in score)
        fo.close()
        
    def test_highest_score(self):
        scorelist = []
        fo = open('highScore.txt','r+')
        for line in fo:
            if len(line)==2 or len(line)==1:
                scorelist.append(int(line[0]))
            else:
                scorelist.append(int(line[0]+line[1]))
        if len(scorelist)>0:
            new_max = max(scorelist)+2
            highest = self.bj.highest_score(new_max)
            self.bj.write_score('highScore.txt',new_max)
            self.assertTrue(highest)
        fo.close()


       
unittest.main()
