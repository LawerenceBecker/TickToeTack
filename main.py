### Import info ###

## Board is a hashmap

### Ideas ###

## Reads the move and plays the best move based on that

import pygame as pg

from board import Board
from cpu import CPU
from uiElements import AreaInput

gameBoard = Board()
cpu = CPU()
pg.init()

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((600,600))
        pg.display.set_caption('Tick Tack Toe')
        self.clock = pg.time.Clock()

        self.sprites = pg.sprite.Group()

        AreaInput(self.sprites, 95, 95, gameBoard, 0)
        AreaInput(self.sprites, 235, 95, gameBoard, 1)
        AreaInput(self.sprites, 375, 95, gameBoard, 2)

        AreaInput(self.sprites, 95, 235, gameBoard, 3)
        AreaInput(self.sprites, 235, 235, gameBoard, 4)
        AreaInput(self.sprites, 375, 235, gameBoard, 5)

        AreaInput(self.sprites, 95, 375, gameBoard, 6)
        AreaInput(self.sprites, 235, 375, gameBoard, 7)
        AreaInput(self.sprites, 375, 375, gameBoard, 8)

        self.font = pg.font.Font(None, 36)
        
    
    def run(self):
        while True:
            # print(f'\nTurn: {gameBoard.turnNum}')
            # gameBoard.printBoard()

            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.QUIT

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if gameBoard.playerTurn == True:
                            for _sprite in self.sprites:
                                if _sprite.rect.collidepoint(pg.mouse.get_pos()):
                                    _sprite.onClick()
                
                
            for _sprite in self.sprites:
                if _sprite.rect.collidepoint(pg.mouse.get_pos()):
                    _sprite.hover()
                else:
                    _sprite.no_hover()
                        
            self.screen.fill('grey')
            backdrop = pg.Rect(90, 90, 420, 420)
            pg.draw.rect(self.screen, 'dark grey', backdrop)
            self.sprites.draw(self.screen)

            playerWinTxt = self.font.render(f'Player', False, 'black')
            self.screen.blit(playerWinTxt, [(95/2)-(playerWinTxt.get_width()/2),130])

            playerWinTxt = self.font.render(f'{gameBoard.playerWin}', False, 'black')
            self.screen.blit(playerWinTxt, [(95/2)-(playerWinTxt.get_width()/2),155])

            
            tieWinTxt = self.font.render(f'Tie', False, 'black')
            self.screen.blit(tieWinTxt, [(95/2)-(tieWinTxt.get_width()/2),270])

            tieWinTxt = self.font.render(f'{gameBoard.tieWin}', False, 'black')
            self.screen.blit(tieWinTxt, [(95/2)-(tieWinTxt.get_width()/2),295])

            
            cpuWinTxt = self.font.render(f'CPU', False, 'black')
            self.screen.blit(cpuWinTxt, [(95/2)-(cpuWinTxt.get_width()/2),410])

            cpuWinTxt = self.font.render(f'{gameBoard.cpuWin}', False, 'black')
            self.screen.blit(cpuWinTxt, [(95/2)-(cpuWinTxt.get_width()/2),435])
            
            pg.display.update()
            self.clock.tick(60)

            if gameBoard.win == True:
                print(f'{gameBoard.winner} won the game!')
                if gameBoard.winner == gameBoard.player: gameBoard.playerWin += 1
                if gameBoard.winner == gameBoard.cpu: gameBoard.cpuWin += 1
                choice = input('Play again? (y/n) \n> ')
                if choice.lower() == 'y':
                    gameBoard.win = False
                    gameBoard.playerTurn = True
                    gameBoard.turnNum = 1
                    gameBoard.hashBoard = [
                        ' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ',]
                    cpu.firstTrun = True

                    for _sprite in self.sprites:
                        if hasattr(_sprite, 'filled'):
                            _sprite.filled = False
                
                elif choice.lower() == 'n':
                    print('Thanks for playing!')
                    break
        
            for _ in gameBoard.hashBoard:
                if _ == ' ':
                    tie = False
                    break
                else:
                    tie = True
        
            if tie == True:
                print('\nThe game is tied')
                gameBoard.tieWin += 1
                choice = input('Play again? (y/n) \n> ')
                if choice.lower() == 'y':
                    gameBoard.win = False
                    gameBoard.playerTurn = True
                    gameBoard.turnNum = 1
                    gameBoard.hashBoard = [
                        ' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ',]
                    cpu.firstTrun = True

                    for _sprite in self.sprites:
                        if hasattr(_sprite, 'filled'):
                            _sprite.filled = False
                    
                elif choice.lower() == 'n':
                    print('Thanks for playing!')
                    break

                
            elif gameBoard.playerTurn == False:
                cpu.pickMove(gameBoard)
                gameBoard.playerTurn = True
                for _sprite in self.sprites:
                    if gameBoard.hashBoard[_sprite.hashIndex] != ' ':
                        _sprite.filled = True
                
if __name__ == '__main__':
    game = Game()
    game.run()