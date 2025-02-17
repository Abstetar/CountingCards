class Player:


    def __init__ (self):

        self._hand = []
        self._handTotal = 0
        self._name = ""
        self._unconvertedAces = 0

    #region properties
    @property
    def hand(self):
        return self._hand
    
    # Do I /need/ a hand setter? Would I ever use it? or am I just always adding cards to the existing list?
    @hand.setter
    def hand(self, listOfCards):
        if not isinstance(listOfCards, list):
            raise TypeError("hand must be a list")
        self._hand = listOfCards

    @hand.deleter
    def hand(self):
        self._hand = []

    @property
    def handTotal(self):
        return self._handTotal
    
    @handTotal.setter
    def handTotal(self, total):
        if not isinstance(total, int):
            raise TypeError("handTotal must be an integer")
        self._handTotal = total

    @handTotal.deleter
    def handTotal(self):
        self._handTotal = 0

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newName):
        if not isinstance(newName, str):
            raise TypeError("name must be a string")
        self._name = newName

    @name.deleter
    def name(self):
        self._name = ""
    #endregion properties


    def calcHandTotal(self):
        total = 0
        ranksInHand = [] ##Shoot do I turn this into a property instead?

        for i in range(len(self.hand)): # Do I want _hand here instead? what is best practice?
            cardRank = self.hand[i][0]
            ranksInHand.append(cardRank)
            total += self.convertCardValue(cardRank)

        total = self.handleAces(total)

        self.handTotal = total
    
    def updateHandTotal(self, newCard):
        # update the hand total with just the new card that was dealt to the player
        newTotal = self.handTotal + self.convertCardValue(newCard[0])
        newTotal = self.handleAces(newTotal)
        self.handTotal = newTotal
        

    def updateHand(self, newCard):
        # update the current player's hand with the new card and then updateHandTotal as well
        self.hand.append(newCard)
        self.updateHandTotal(newCard)


    def handleAces(self, total):
        #extract the ace case code to be easily re-used
        updatedTotal = total

        while updatedTotal > 21 and self._unconvertedAces > 0:
            updatedTotal -= 10
            self._unconvertedAces -= 1


        return updatedTotal
    
    def convertCardValue(self, cardRank):
        convertedValue = 0
        if cardRank in {'J','Q','K'}:
            convertedValue = 10
        elif cardRank == 'A':
            convertedValue = 11
            self._unconvertedAces += 1
        else:
            convertedValue = int(cardRank)
        return convertedValue



    # I Think I'm going to want an updateHand and an updateHandTotal function as well

    # Refactor everything to use this new Player Class, and move the game logic out of the deck class.
    # Create a new "Game" class to hold all of the deck and player info the current game? 
    # Should this Game class also have the Deal and handTotal calculation functions? 

    