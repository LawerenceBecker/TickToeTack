### Import info ###

## Board is a hashmap

### Ideas ###

## Reads the move and plays the best move based on that
## Tries to play a set moveset based on the first move
## Use a point system to way what choice it should make

from board import Board
from cpu import CPU

gameBoard = Board()
cpu = CPU()

while True:
    print(f'\nTurn: {gameBoard.turnNum}')
    gameBoard.printBoard()

    for _ in gameBoard.hashBoard:
        if _ == ' ':
            tie = False
            break
        else:
            tie = True

    if tie == True:
        print('The game is tied')
        choice = input('Play again? (y/n) \n> ')
        if choice.lower() == 'y':
            gameBoard.win = False
            gameBoard.playerTurn = True
            gameBoard.turnNum = 1
            
        elif choice.lower() == 'n':
            print('Thanks for playing!')
            break
    
    elif gameBoard.win == True:
        print(f'{gameBoard.winner} won the game!')
        choice = input('Play again? (y/n) \n> ')
        if choice.lower() == 'y':
            gameBoard.win = False
            gameBoard.playerTurn = True
            gameBoard.turnNum = 1
            
        elif choice.lower() == 'n':
            print('Thanks for playing!')
            break
        
    elif gameBoard.playerTurn == True: 
        print('\nPlayer Turn')
        choice = input('> ')
        gameBoard.addInput(choice, gameBoard.player)
        
    elif gameBoard.playerTurn == False:
        print('\nCPU Turn')
        cpu.pickMove(gameBoard)
        gameBoard.playerTurn = True
        gameBoard.turnNum += 1
        
        