#author - Yike Chen and Yejia Li

import unittest
from SoloBlackjack import *
from Cards import *


class Test_BlackJack(unittest.TestCase):

    def setUp(self):
        self.bj = BlackJack()
        self.card = Card('A','S')
        self.choice1='y'
        self.choice2='N'
        self.slot1 = 1
        self.slot2 = 100
        self.slot3 = 'a'
        self.disposal = [1,2,3,4,5]

    # No need to test a function which does nothing but print out stuff
##    def test_initial_display(self):
##        self.bj.initial_display()

##    def test_make_a_move(self):
##        self.bj.make_a_move(self.card)

##    def test_get_value(self):
##        value = self.bj.get_value(self.card)
##        self.assertEqual(value,1)


##    def test_error_checking(self):
##        self.bj.error_checking(self.choice1,self.slot1)
##        self.bj.error_checking(self.choice1,self.slot3)
##        self.assertEqual(value,1)

##    def test_isDisposalFull(self):
##        print self.bj.isDisposalFull()

    def test_write_score(self):
        self.bj.write_score('14')
        
unittest.main()
