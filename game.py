from player import Player
from deck import Deck

class Game:

    def __init__(self, numPlayers=1, numDecks=1):
        # What do I want to do here?
        self._numPlayers = numPlayers
        #Do I need to give the players names/numbers in order to access them correctly or can I just index to them?
        #How is adding/removing players going to affect this? can I simply add / remove or do I need to keep track of player number
        self._players = [ Player() for i in range(numPlayers) ]
        self._gameDeck = Deck(numDecks)

    #region properties

    @property
    def numPlayers(self):
        return self._numPlayers

    @numPlayers.setter
    def numPlayers(self, numPlayers):
        if not isinstance(numPlayers, int):
            raise TypeError("numPlayers must be an integer")
        
        self._numPlayers = numPlayers

    @numPlayers.deleter
    def numPlayers(self):
        del self._numPlayers

    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, newPlayers):
        if not isinstance(newPlayers, dict):
            raise TypeError("newPlayers must be a dict")
        self._players = newPlayers
    
    @players.deleter
    def players(self):
        del self._players

    @property
    def gameDeck(self):
        return self._gameDeck

    @gameDeck.setter
    def gameDeck(self, newDeck):
        self._gameDeck = newDeck

    @gameDeck.deleter
    def gameDeck(self):
        del self._gameDeck

    #endregion properties


    # Deal function should stay in the deck (I think that makes the most sense)

    def calcHandTotal(self, player):
        total = 0
        ranksInHand = []

        playerHand = player.hand

        for i in range(len(playerHand)): # Do I want _hand here instead? what is best practice?
            cardRank = playerHand
            ranksInHand.append(cardRank)
            if cardRank in {'J','Q','K'}:
                total += 10
            elif cardRank == 'A':
                total += 11
            else:
                total += int(cardRank)

        total = self.handleAces(total, ranksInHand)

        return total
    
    # Not sure I need the numCards parameter, I think I might just want to call this method every time I want to deal a single call
    # Or do I just loop in this method? -- Though theoretically I will only ever deal one card at a time to a player
    def dealToPlayer(self, playerNumber, numCards=1): 
        if len(self.gameDeck.cards) < numCards:
            return ("Not enough cards left in deck to deal cards")
        selectedPlayer = self.players[playerNumber - 1]
        # selectedPlayer.hand.append(self.gameDeck.deal())
        newCard = self.gameDeck.deal()
        selectedPlayer.updateHand(newCard)


    #### TODO!!
    def addPlayers(self, numPlayers):
        self._players 

    ### TODO!!
    def removePlayers(self, playerNumber):
        ## Remove that player from the game
        ## How I do this will depend on how the collection works for the players
        return 0

    def printHands(self):
        
        # for i in range(self.numPlayers):

        
        
        
        return 
        # How do I want to represent this?? -- Do I want to have all of these on separate lines? Probably
        # player 1: AH, 4C, 3D Total: 18
        # player 2: 6S, 3H, 9D
        # dealer:   AD, KC 

        # Use handTotal() to add total to the end of the list of cards

    def printPlayerHand(self, playerNumber):
        selectedPlayer = self.players[playerNumber - 1]
        print(f"player{playerNumber}: {selectedPlayer.hand} total: {selectedPlayer.handTotal}")