import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.suit}, {self.rank}"
    
class Deck():
    def __init__(self):
        self.cards=[]

        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = [1,2,3,4,5,6,7,8,9,10]
        for i in range(len(suits)):
            for j in range(len(ranks)):
                self.cards.append(Card(suit=suits[i], rank=ranks[j]))

    def shuffle(self):
        random.shuffle(self.cards)


    def print(self):
        for card in self.cards:
            print(str(card))
    
    def get_cards(self, num_cards = 1):
        given_cards = []
        for i in range(num_cards):
            given_cards.append(self.cards.pop(0))
        return given_cards
        




    
