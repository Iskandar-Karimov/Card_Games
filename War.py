from Card import Card
from Card import Deck

class War():
    def __init__(self):
        self.player1 = []
        self.player2= []
        self.deck = Deck()
        self.deck.shuffle()
        self.player1_wins = 0
        self.player2_wins = 0
        self.player1 = self.deck.cards[0: len(self.deck.cards)//2]
        self.player2 = self.deck.cards[len(self.deck.cards) //2:]

    def compare_top(self):
        pulled_p1 = self.player1.pop(0)
        pulled_p2 = self.player2.pop(0)
        print(f"Player 1 - {pulled_p1}")
        print(f"Player 2 - {pulled_p2}")
        if pulled_p1.rank > pulled_p2.rank:
            print("Player 1 won this round!\n")
            self.player1_wins += 1
            self.print()
        elif pulled_p1.rank == pulled_p2.rank:
            print("This round was a tie\n")
            self.print()
        else:
            print("Player 2 won this round!\n")
            self.player2_wins += 1
            self.print()
        
    
    def game(self):
        round_number = 1
        while len(self.player1) != 0 or len(self.player2) != 0:
            __test = input("")
            print(f"\033[1mROUND {round_number}\033[0m") 
            self.compare_top()
            round_number += 1
        if self.player1_wins > self.player2_wins:
            print("PLAYER 1 WINS!")
        elif self.player2_wins > self.player1_wins:
            print("PLAYER 2 WINS!")
        else:
            print("IT'S A TIE.")
    
    
    
    def print(self):
        print("PLAYER 1:")
        for card in self.player1:
            print(str(card))
        
        print("\nPLAYER 2:")
        for card in self.player2:
            print(str(card))


game = War()
game.game()