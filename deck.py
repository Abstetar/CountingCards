import itertools
import random

class Deck:
    
    suits = ['H', 'D', 'S', 'C']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, numberOfDecks = 1):

        self._cards = [(rank, suit) for rank, suit in itertools.product(self.ranks, self.suits)] * numberOfDecks

    @property
    def cards(self):
        return self._cards

    # This function should only pick a random card from the deck and remove it from the list
    
    # def deal(self, numPlayers=1, numCards=1):
    #     if (numPlayers * numCards > len(self.cards)): 
    #         print("Too few cards remaining to deal out hands")
    #     else:
    #         for i in range(numPlayers):
    #             self.playersAndHands[f'player{i+1}'] = []
    #             for j in range(numCards):
    #                 card = random.choice(self.cards)
    #                 self.playersAndHands[f'player{i+1}'].append(card)
    #                 self.cards.remove(card)
    #             print(f"player{i+1}: {self.playersAndHands[f'player{i+1}']}")

    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
    
