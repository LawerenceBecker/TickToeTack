
class CPU:
    def __init__(self):
        self.firstTrun = True

    def pickMove(self, board):
        if self.firstTrun == True: self.turn1(board)
        else:
            pWinSoon = self.checkForPWin(board)
            if pWinSoon[0] == True:
                
                board.addInput(pWinSoon[1], board.cpu)
            else:
                
                cWinSoon = self.checkForSelfWin(board)
                if cWinSoon[0] == True:
                    
                    board.addInput(cWinSoon[1], board.cpu)
                else:
                    
                    r = 0
                    c = 0
                    for _ in board.hashBoard:
                        if _ == ' ':
                            board.addInput(f'{r} {c}', board.cpu)
                            break
                        if r == 2:
                            c += 1
                            r = 0
                        else:
                            r += 1

    def checkForSelfWin(self, board):

        ## Horizontal
        if board.hashBoard[0] == board.hashBoard[1] and board.hashBoard[0] == board.cpu:
            if board.hashBoard[2] != board.player:
                return True, '2 0'
        if board.hashBoard[3] == board.hashBoard[4] and board.hashBoard[4] == board.cpu:
            if board.hashBoard[5] != board.player:
                return True, '2 1'
        if board.hashBoard[6] == board.hashBoard[7] and board.hashBoard[6] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, '2 2'

        ## Vertical
        if board.hashBoard[0] == board.hashBoard[3] and board.hashBoard[0] == board.cpu:
            if board.hashBoard[6] != board.player:
                return True, '0 2'
        if board.hashBoard[1] == board.hashBoard[4] and board.hashBoard[1] == board.cpu:
            if board.hashBoard[7] != board.player:
                return True, '1 2'
        if board.hashBoard[2] == board.hashBoard[5] and board.hashBoard[2] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, '2 2'

        ## Diagonal
        if board.hashBoard[0] == board.hashBoard[4] and board.hashBoard[0] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, '2 2'
        if board.hashBoard[2] == board.hashBoard[4] and board.hashBoard[2] == board.cpu:
            if board.hashBoard[6] != board.player:            
                return True, '0 2'

        return False, ''
        
    def checkForPWin(self, board):
        
        ## Horizontal
        if board.hashBoard[0] == board.hashBoard[1] and board.hashBoard[0] == board.player:
            if board.hashBoard[2] != board.cpu:
                return True, '2 0'
        if board.hashBoard[3] == board.hashBoard[4] and board.hashBoard[3] == board.player:
            if board.hashBoard[5] != board.cpu:
                return True, '2 1'
        if board.hashBoard[6] == board.hashBoard[7] and board.hashBoard[6] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, '2 2'

        ## Horizontal Middle
        if board.hashBoard[0] == board.hashBoard[2] and board.hashBoard[0] == board.player:
            if board.hashBoard[1] != board.cpu:
                return True, '1 0'
        if board.hashBoard[3] == board.hashBoard[5] and board.hashBoard[3] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, '1 1'
        if board.hashBoard[6] == board.hashBoard[8] and board.hashBoard[6] == board.player:
            if board.hashBoard[7] != board.cpu:
                return True, '1 2'

        ## Vertical
        if board.hashBoard[0] == board.hashBoard[3] and board.hashBoard[0] == board.player:
            if board.hashBoard[6] != board.cpu:
                return True, '0 2'
        if board.hashBoard[1] == board.hashBoard[4] and board.hashBoard[1] == board.player:
            if board.hashBoard[7] != board.cpu:
                return True, '1 2'
        if board.hashBoard[2] == board.hashBoard[5] and board.hashBoard[2] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, '2 2'

        ## Vertical Middle
        if board.hashBoard[0] == board.hashBoard[6] and board.hashBoard[0] == board.player:
            if board.hashBoard[3] != board.cpu:
                return True, '0 1'
        if board.hashBoard[1] == board.hashBoard[7] and board.hashBoard[1] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, '1 1'
        if board.hashBoard[2] == board.hashBoard[8] and board.hashBoard[2] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, '2 1'
        

        ## Diagonal
        if board.hashBoard[0] == board.hashBoard[4] and board.hashBoard[0] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, '2 2'
        if board.hashBoard[2] == board.hashBoard[4] and board.hashBoard[2] == board.player:
            if board.hashBoard[6] != board.cpu:            
                return True, '0 2'

        return False, ''
            
    def turn1(self, board):
        if board.hashBoard[4] == board.player: board.addInput('0 0', board.cpu)
        elif board.hashBoard[0] == board.player or board.hashBoard[2] == board.player or board.hashBoard[6] == board.player or board.hashBoard[8] == board.player: board.addInput('1 1', board.cpu)
        elif board.hashBoard[1] == board.player: board.addInput('1 2', board.cpu)
        elif board.hashBoard[7] == board.player: board.addInput('1 0', board.cpu)
        elif board.hashBoard[3] == board.player: board.addInput('2 1', board.cpu)
        elif board.hashBoard[5] == board.player: board.addInput('0 2', board.cpu)
        
        self.firstTrun = False