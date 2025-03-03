import itertools
import random

class Deck:
    
    suits = ['H', 'D', 'S', 'C']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, numberOfDecks = 1):
        # Convert Cards into an object at some point? Make printing them out a little easier and keeping track of them
        self._cards = [(rank, suit) for rank, suit in itertools.product(self.ranks, self.suits)] * numberOfDecks

    @property
    def cards(self):
        return self._cards


    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
    
