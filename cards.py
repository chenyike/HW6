def test_deal(self):
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
def test_deal(self):
        # get the last card from the pile
        get_deck = self.deck.get_deck()
        last_card = get_deck[-1].rank+get_deck[-1].suit
def test_deal(self):
        # get the last card from the pile
       rom cards import *

class Solitaire(object):

    def tableaus(self):
        disposal=[]
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

  
