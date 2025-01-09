from Card import Card
from Card import Deck

import random

class Player():
    def __init__(self, cards):
        self.cards = cards
        self.score = 0

    def print(self):
        for card in self.cards:
            print(str(card))

    def check_cards(self, rank):
        found_cards = []
        index = 0
        while index < len(self.cards):
            if self.cards[index].rank == rank:
                found_cards.append(self.cards.pop(index))
            else:
                index += 1
        return found_cards
    
    def add_cards(self, found_cards):
        self.cards = self.cards + found_cards

    def check_for_four_cards(self):
        for i in range(1, 11):
            count = sum(card.rank == i for card in self.cards)
            if count == 4:
                self.cards = [card for card in self.cards if card.rank != i]
                self.score += 1
    
    

# deck = Deck()
# deck.shuffle()
# myPlayer = Player(cards = deck.get_cards(5))
# myPlayer2 = Player(cards= deck.get_cards(5))
# print("Player 1:")
# myPlayer.print()
# print("\nPlayer 2")
# myPlayer2.print()
# returnedCards = myPlayer.check_cards(8)
# print("Returned card from Player 1:")
# for card in returnedCards:
#     print(str(card))
# print()
# print("Player 1's new cards:")
# myPlayer.print()

# print("\nPlayer 2's new cards:")
# myPlayer2.add_cards(returnedCards)
# myPlayer2.print()

#Initializing
deck = Deck()
deck.shuffle()
Human = Player(cards=deck.get_cards(5))
Computer = Player(cards=deck.get_cards(5))

#Human's turn, guessing from computer
while len(Human.cards) > 0 and len(Computer.cards) > 0:
    print("Here are your cards:")
    Human.print()
    requested_card = int(input("\nWhat card do you want to request?: "))
    found = Computer.check_cards(requested_card)
    print("The opponent had these cards:")
    if found == []:
        print("\nGO FISH!\n")
        Human.add_cards(deck.get_cards())
    go = input("")
    for card in found:
        print(card)
    Human.add_cards(found_cards=found)
    print(f"\nNew Cards: ")
    Human.print()
    Human.check_for_four_cards()
    print("")

    #Computer's turn, guessing from human
    computerturn = input("Computer's Turn (Enter to continue): ")
    requested_card2 = Computer.cards[0]
    found2 = Human.check_cards(requested_card2.rank)
    print(f"The computer guessed this card rank: {requested_card2.rank}")
    if found2 == []:
        print("\nGO FISH!\n")
        Computer.add_cards(deck.get_cards())
    Computer.add_cards(found_cards=found2)
    Computer.check_for_four_cards()
    print(" ")
