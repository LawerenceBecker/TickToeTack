import pygame as pg

class AreaInput(pg.sprite.Sprite):
    def __init__(self, groups, x, y, board, hashIndex):
        super().__init__(groups)

        self.image = pg.Surface((130,130))
        self.rect = self.image.get_rect(topleft = (x, y))

        self.hashIndex = hashIndex
        self.filled = False

        self.board = board
        
        self.font = pg.font.Font(None, 200)
        
    def hover(self):
        self.image.fill('#dbdbdb')
        if self.filled == True:
            txtSurf = self.font.render(self.board.hashBoard[self.hashIndex], False, 'Black')
        else:
            txtSurf = self.font.render(self.board.player, False, '#7d7d7d')
        self.image.blit(txtSurf, [
            (self.image.get_width()/2)-(txtSurf.get_width()/2),
            (self.image.get_height()/2)-(txtSurf.get_height()/2)])
            

    def no_hover(self):
        self.image.fill('light grey')
        if self.filled == True:
            txtSurf = self.font.render(self.board.hashBoard[self.hashIndex], False, 'Black')
            self.image.blit(txtSurf, [
            (self.image.get_width()/2)-(txtSurf.get_width()/2),
            (self.image.get_height()/2)-(txtSurf.get_height()/2)])

    def onClick(self):
        if self.filled == False:
            self.filled = True
            self.board.addInput(self.hashIndex, self.board.player)

class Buttons(pg.sprite.Sprite):
    def __init__(self, groups, x, y, text, board, cpu, game=None):
        super().__init__(groups)

        self.image = pg.Surface((220,110))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.sprites = groups
        self.game = game

        self.text = text
        self.board = board
        self.done = False

        self.font = pg.font.Font(None, 100)
        self.txtSurf = self.font.render(self.text, False, 'Black')

        self.cpu = cpu
        
    def hover(self):
        self.image.fill('#a8a8a8')
        foreRect = pg.Rect(10, 10, 200, 90)
        pg.draw.rect(self.image, '#cfcfcf', foreRect)
        self.image.blit(self.txtSurf, [
            (self.image.get_width()/2)-(self.txtSurf.get_width()/2),
            (self.image.get_height()/2)-(self.txtSurf.get_height()/2)
        ])
            

    def no_hover(self):
        self.image.fill('#949494')
        foreRect = pg.Rect(10, 10, 200, 90)
        pg.draw.rect(self.image, '#b8b8b8', foreRect)
        self.image.blit(self.txtSurf, [
            (self.image.get_width()/2)-(self.txtSurf.get_width()/2),
            (self.image.get_height()/2)-(self.txtSurf.get_height()/2)
        ])

    def onClick(self):
        if self.text == 'x':
            self.board.player = 'x'
            self.board.cpu = 'o'
        elif self.text == 'Yes' or self.text == 'Yes ':
            self.game.restart = False
            for _sprite in self.sprites:
                _sprite.kill()
            AreaInput(self.sprites, 95, 95, self.board, 0)
            AreaInput(self.sprites, 235, 95, self.board, 1)
            AreaInput(self.sprites, 375, 95, self.board, 2)
    
            AreaInput(self.sprites, 95, 235, self.board, 3)
            AreaInput(self.sprites, 235, 235, self.board, 4)
            AreaInput(self.sprites, 375, 235, self.board, 5)
    
            AreaInput(self.sprites, 95, 375, self.board, 6)
            AreaInput(self.sprites, 235, 375, self.board, 7)
            AreaInput(self.sprites, 375, 375, self.board, 8)

        elif self.text == 'No' or self.text == 'No ':
            pg.quit()
        else:
            self.board.player = 'o'
            self.board.cpu = 'x'
        
        self.done = True