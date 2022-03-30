class Board():
    def __init__(self):
        print('### input all commands as 0,0 0,1 1,0 ...etc ###')
        
        self.hashBoard = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',]

        choice = input('Xs or Os? (x/o) \n> ')
        if choice.lower() == 'x':
            self.player = 'x'
            self.cpu = 'o'
        elif choice.lower() == 'o':
            self.player = 'o'
            self.cpu = 'x'

        self.playerTurn = True
        self.win = False
        self.winner = ''
        self.turnNum = 1

    def printBoard(self):
        row = 0

        textPrint = ' '
        for i, _ in enumerate(self.hashBoard):
            textPrint += _
            
            if row == 2:
                row = 0
                print(textPrint)
                textPrint = ' '
                if i != 8:                    
                    print('-----------')
            else:
                row += 1
                
                textPrint += ' | '

    def addInput(self, input, mark):

        if  len(input) != 3 or int(input[0]) >= 3 or int(input[2]) >= 3:
            print('Not possiable input')
            return

        toIndex = 0
        toIndex += int(input[0])
        
        if int(input[2]) == 0: pass
        elif int(input[2]) == 1: toIndex += 3
        elif int(input[2]) == 2: toIndex += 6

        if self.hashBoard[toIndex] == ' ':
            self.hashBoard[toIndex] = mark
            self.playerTurn = False
            self.checkWins()
        else:
            print('That position already has a mark in it')

    def checkWins(self):

        ## Horizontal
        if self.hashBoard[0] == self.hashBoard[1] and self.hashBoard[0] == self.hashBoard[2]:
            if self.hashBoard[0] != ' ':
                self.win = True
                self.winner = self.hashBoard[0]
        elif self.hashBoard[3] == self.hashBoard[5] and self.hashBoard[4] == self.hashBoard[5]:
            if self.hashBoard[3] != ' ':
                self.win = True
                self.winner = self.hashBoard[3]
        elif self.hashBoard[6] == self.hashBoard[7] and self.hashBoard[6] == self.hashBoard[8]:
            if self.hashBoard[6] != ' ':
                self.win = True
                self.winner = self.hashBoard[6]

        ## Vertical
        elif self.hashBoard[0] == self.hashBoard[3] and self.hashBoard[0] == self.hashBoard[6]:
            if self.hashBoard[0] != ' ':
                self.win = True
                self.winner = self.hashBoard[0]
        elif self.hashBoard[1] == self.hashBoard[4] and self.hashBoard[1] == self.hashBoard[7]:
            if self.hashBoard[1] != ' ':
                self.win = True
                self.winner = self.hashBoard[1]
        elif self.hashBoard[2] == self.hashBoard[5] and self.hashBoard[2] == self.hashBoard[8]:
            if self.hashBoard[2] != ' ':
                self.win = True
                self.winner = self.hashBoard[2]

        ## Diagonal
        elif self.hashBoard[0] == self.hashBoard[4] and self.hashBoard[0] == self.hashBoard[8]:
            if self.hashBoard[0] != ' ':
                self.win = True
                self.winner = self.hashBoard[0]
        elif self.hashBoard[2] == self.hashBoard[4] and self.hashBoard[2] == self.hashBoard[6]:
            if self.hashBoard[2] != ' ':
                self.win = True
                self.winner = self.hashBoard[2]