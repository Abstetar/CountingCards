from player import Player
from deck import Deck

class Game:

    def __init__(self, numPlayers=1, numDecks=1):
        self._numPlayers = numPlayers
        #Do I need to give the players names/numbers in order to access them correctly or can I just index to them?
        #How is adding/removing players going to affect this? can I simply add / remove or do I need to keep track of player number
        self._players = [ Player(f"Player {i+1}") for i in range(numPlayers) ]
        self._gameDeck = Deck(numDecks)
        self._dealer = Player()

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

    def runGame(self):
        self.dealToPlayer(-1, 2)
        self.printDealerHand(False, False)
        for i in range(self.numPlayers):

            hasStood = False
            currentPlayer = self.players[i]
            self.dealToPlayer(i, 2)
            self.printPlayerHand(i)

            while(not hasStood):
                if currentPlayer.handTotal > 21:
                    print("\nBust. Better luck next time")
                    hasStood = True
                elif currentPlayer.handTotal == 21:
                    print("\nCongrats! You've made 21!")
                    hasStood = True
                else:
                    nextMove = input("\nWould you like to 'hit' or 'stand'?: ").lower().strip()
                    if(nextMove == "hit"):
                        self.dealToPlayer(i, 1)
                        self.printPlayerHand(i)
                    else: 
                        hasStood = True

        # Dealers turn
        print("\nDealer's Turn")
        self.printDealerHand(True, True)
        if self._dealer.handTotal >= 17:
            dealerHasStood = True
        else:
            dealerHasStood = False

        while(not dealerHasStood):
            self.dealToPlayer(-1, 1)
            self.printDealerHand(True, True)
            
            if self._dealer.handTotal >= 17:
                dealerHasStood = True


        # Determine winners and end the game -- Extract this to a separate method

        # Grab Dealer's hand total
        dealersFinalTotal  = self._dealer.handTotal

        # Compare that value against all of the players' hand totals 
        for player in self.players:
            # If Player's handTotal >= 22 - Bust
            if player.handTotal >= 22:
                print(f"\n{player.name} busted!")
            # else If Player's hand total is greater than Dealer's Hand Total - Player wins
            elif player.handTotal > dealersFinalTotal:
                print(f"\n{player.name} won!")
            # Player and dealer had the same total so it was a push
            elif player.handTotal == dealersFinalTotal:
                print(f"\n{player.name} pushed!")
            # else - player loses
            else:
                print(f"\n{player.name} lost!")
        

    def calcHandTotal(self, player):
        total = 0
        ranksInHand = []

        playerHand = player.hand

        for i in range(len(playerHand)):
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
            return ("\nNot enough cards left in deck to deal cards")
        if playerNumber == -1:
            selectedPlayer = self._dealer
        else:
            selectedPlayer = self.players[playerNumber]

        for i in range(numCards):
            newCard = self.gameDeck.deal()
            selectedPlayer.updateHand(newCard)


    #### TODO!!
    def addPlayers(self, numPlayers):
        return

    ### TODO!!
    def removePlayers(self, playerNumber):
        ## Remove that player from the game
        ## How I do this will depend on how the collection works for the players
        return

    ### TODO!! Should print all players' + dealer's hands -- Not sure if I still need this to happen or not
    def printHands(self):
        # for i in range(self.numPlayers):
        # self.printDealerHand()
        return 

    def printPlayerHand(self, playerNumber):
        selectedPlayer = self.players[playerNumber]
        print(f"\n{selectedPlayer.name}: {selectedPlayer.hand} total: {selectedPlayer.handTotal}")

    def printDealerHand(self, revealHoleCard, showTotal):
        dealerHand = "\nDealer: "
        if not revealHoleCard:
            dealerHand += f"[{self._dealer.hand[0]}, ('X', 'X')]"
        else:
            dealerHand += f"{self._dealer.hand}"
        
        if showTotal:
            dealerHand += f" total: {self._dealer.handTotal}"
        print(dealerHand)
    