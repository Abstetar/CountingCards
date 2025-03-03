from game import Game

if __name__ == "__main__":

    game = Game() # Not sure if there is a better way to initialize this but we'll go with this for now
    startNewGame = True
    continueGame = True
    initialLoop = True

    while continueGame:
        if initialLoop:
            print("\nWelcome to Counting Cards!")
            initialLoop = False
        else:
            startNewGame = input("\nwould you like to start a new game? (y/n): ").lower().strip() == 'y'
            
        if startNewGame:
            # I think that for now, we will always assume it will be new players in the game
            # Lets handle returning players in the future
            
            numberOfPlayers = int(input("\nHow many players would like to play: "))
            numberOfDecks = int(input("How many decks would you like to use: "))
            game = Game((numberOfPlayers), numberOfDecks)
            startNewGame = False

        # At this point I think I should call a method in the Game class and handle the logic in there instead
        game.runGame()
        continueGame = input("\nwould you like to continue playing? (y/n): ").lower().strip() == 'y'

