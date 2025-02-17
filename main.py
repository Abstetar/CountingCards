from game import Game

if __name__ == "__main__":

    game = Game(2, 2)

    print("number of cards in the gameDeck: ", len(game.gameDeck.cards) )


    game.dealToPlayer(1, 1)
    game.dealToPlayer(1, 1)
    game.dealToPlayer(1, 1)

    game.dealToPlayer(2, 1)
    game.dealToPlayer(2, 1)
    game.dealToPlayer(2, 1)

    game.printPlayerHand(1)
    game.printPlayerHand(2)






    # for card in newDeck._cards:
    #     print(f"{card[0]}{card[1]}")

    # newDeck.deal(2, 3)

    # print(newDeck.handTotal(1))
    # print(newDeck.handTotal(2))

    # I think this class should have a loop that handles instances of "Games"
    # I think from this class (in the loop) you should be able to continue dealing rounds
    # of "Games" with the same players, add/remove players, and end the game (the loop)

