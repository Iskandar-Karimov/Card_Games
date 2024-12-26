import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"Card: {self.suit}, {self.rank}"
    
class Deck():
    def __init__(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = [1,2,3]
        self.cards = []
        for i in range(len(suits)):
            for j in range(len(ranks)):
                self.cards.append(Card(suit=suits[i], rank=ranks[j]))

    def shuffle(self):
        random.shuffle(self.cards)


    def print(self):
        for card in self.cards:
            print(str(card))
