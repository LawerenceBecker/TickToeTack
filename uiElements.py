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
        