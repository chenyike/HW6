#author - Yike Chen and Yejia Li

import unittest
from SoloBlackjack import *


class Test_BlackJack(unittest.TestCase):

    def setUp(self):
        self.bj = BlackJack()


    # No need to test a function which does nothing but print out stuff
    def test_initial_display(self):
        self.bj.initial_display()
        
    
    
        
unittest.main()
