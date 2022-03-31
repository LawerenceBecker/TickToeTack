
class CPU:
    def __init__(self):
        self.firstTrun = True

    def pickMove(self, board):
        if self.firstTrun == True: self.turn1(board)
        else:
            cWinSoon = self.checkForSelfWin(board)
            if cWinSoon[0] == True:
                    
                board.addInput(cWinSoon[1], board.cpu)
            else:
                pWinSoon = self.checkForPWin(board)
                if pWinSoon[0] == True:
                
                    board.addInput(pWinSoon[1], board.cpu)
                
                else:
                    if board.hashBoard[0] == board.cpu and board.hashBoard[1] == ' ' and board.hashBoard[2] == ' ': board.addInput(2, board.cpu)
                    elif board.hashBoard[0] == board.cpu and board.hashBoard[3] == ' ' and board.hashBoard[6] == ' ': board.addInput(6, board.cpu)
                        
                    elif board.hashBoard[2] == board.cpu and board.hashBoard[1] == ' ' and board.hashBoard[0] == ' ': board.addInput(0, board.cpu)
                    elif board.hashBoard[6] == board.cpu and board.hashBoard[3] == ' ' and board.hashBoard[0] == ' ': board.addInput(0, board.cpu)

                    elif board.hashBoard[8] == board.cpu and board.hashBoard[5] == ' ' and board.hashBoard[2] == ' ': board.addInput(2, board.cpu)
                    elif board.hashBoard[2] == board.cpu and board.hashBoard[5] == ' ' and board.hashBoard[8] == ' ': board.addInput(8, board.cpu)

                    elif board.hashBoard[8] == board.cpu and board.hashBoard[7] == ' ' and board.hashBoard[6] == ' ': board.addInput(6, board.cpu)
                    elif board.hashBoard[6] == board.cpu and board.hashBoard[7] == ' ' and board.hashBoard[8] == ' ': board.addInput(8, board.cpu)
                        
                        
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
                return True, 2
        if board.hashBoard[3] == board.hashBoard[4] and board.hashBoard[4] == board.cpu:
            if board.hashBoard[5] != board.player:
                return True, 5
        if board.hashBoard[6] == board.hashBoard[7] and board.hashBoard[6] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, 8

        ## Vertical
        if board.hashBoard[0] == board.hashBoard[3] and board.hashBoard[0] == board.cpu:
            if board.hashBoard[6] != board.player:
                return True, 6
        if board.hashBoard[1] == board.hashBoard[4] and board.hashBoard[1] == board.cpu:
            if board.hashBoard[7] != board.player:
                return True, 7
        if board.hashBoard[2] == board.hashBoard[5] and board.hashBoard[2] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, 8

        ## Diagonal
        if board.hashBoard[0] == board.hashBoard[4] and board.hashBoard[0] == board.cpu:
            if board.hashBoard[8] != board.player:
                return True, 8
        if board.hashBoard[2] == board.hashBoard[4] and board.hashBoard[2] == board.cpu:
            if board.hashBoard[6] != board.player:            
                return True, 6

        return False, ''
        
    def checkForPWin(self, board):
        
        ## Horizontal
        if board.hashBoard[0] == board.hashBoard[1] and board.hashBoard[0] == board.player:
            if board.hashBoard[2] != board.cpu:
                return True, 2
        if board.hashBoard[3] == board.hashBoard[4] and board.hashBoard[3] == board.player:
            if board.hashBoard[5] != board.cpu:
                return True, 5
        if board.hashBoard[6] == board.hashBoard[7] and board.hashBoard[6] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, 8

        ## Horizontal Inverse
        if board.hashBoard[2] == board.hashBoard[1] and board.hashBoard[2] == board.player:
            if board.hashBoard[0] != board.cpu:
                return True, 0
        if board.hashBoard[5] == board.hashBoard[4] and board.hashBoard[5] == board.player:
            if board.hashBoard[3] != board.cpu:
                return True, 3
        if board.hashBoard[8] == board.hashBoard[7] and board.hashBoard[8] == board.player:
            if board.hashBoard[6] != board.cpu:
                return True, 6

        ## Horizontal Middle
        if board.hashBoard[0] == board.hashBoard[2] and board.hashBoard[0] == board.player:
            if board.hashBoard[1] != board.cpu:
                return True, 1
        if board.hashBoard[3] == board.hashBoard[5] and board.hashBoard[3] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, 4
        if board.hashBoard[6] == board.hashBoard[8] and board.hashBoard[6] == board.player:
            if board.hashBoard[7] != board.cpu:
                return True, 7

        ## Vertical
        if board.hashBoard[0] == board.hashBoard[3] and board.hashBoard[0] == board.player:
            if board.hashBoard[6] != board.cpu:
                return True, 6
        if board.hashBoard[1] == board.hashBoard[4] and board.hashBoard[1] == board.player:
            if board.hashBoard[7] != board.cpu:
                return True, 7
        if board.hashBoard[2] == board.hashBoard[5] and board.hashBoard[2] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, 8

        ## Vertical Inverse
        if board.hashBoard[6] == board.hashBoard[3] and board.hashBoard[6] == board.player:
            if board.hashBoard[0] != board.cpu:
                return True, 0
        if board.hashBoard[7] == board.hashBoard[4] and board.hashBoard[7] == board.player:
            if board.hashBoard[1] != board.cpu:
                return True, 1
        if board.hashBoard[8] == board.hashBoard[5] and board.hashBoard[8] == board.player:
            if board.hashBoard[2] != board.cpu:
                return True, 2

        ## Vertical Middle
        if board.hashBoard[0] == board.hashBoard[6] and board.hashBoard[0] == board.player:
            if board.hashBoard[3] != board.cpu:
                return True, 3
        if board.hashBoard[1] == board.hashBoard[7] and board.hashBoard[1] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, 4
        if board.hashBoard[2] == board.hashBoard[8] and board.hashBoard[2] == board.player:
            if board.hashBoard[5] != board.cpu:
                return True, 5
        

        ## Diagonal
        if board.hashBoard[0] == board.hashBoard[4] and board.hashBoard[0] == board.player:
            if board.hashBoard[8] != board.cpu:
                return True, 8
        if board.hashBoard[2] == board.hashBoard[4] and board.hashBoard[2] == board.player:
            if board.hashBoard[6] != board.cpu:            
                return True, 6

        ## Diagonal Inverse
        if board.hashBoard[8] == board.hashBoard[4] and board.hashBoard[8] == board.player:
            if board.hashBoard[0] != board.cpu:
                return True, 0
        if board.hashBoard[6] == board.hashBoard[4] and board.hashBoard[6] == board.player:
            if board.hashBoard[2] != board.cpu:            
                return True, 2

        ## Diagonal Middle
        if board.hashBoard[0] == board.hashBoard[8] and board.hashBoard[0] == board.player:
            if board.hashBoard[4] != board.cpu:
                return True, 4
        if board.hashBoard[2] == board.hashBoard[6] and board.hashBoard[2] == board.player:
            if board.hashBoard[4] != board.cpu:            
                return True, 4

        return False, ''
            
    def turn1(self, board):
        if board.hashBoard[4] == board.player: board.addInput(0, board.cpu)
        elif board.hashBoard[0] == board.player or board.hashBoard[2] == board.player or board.hashBoard[6] == board.player or board.hashBoard[8] == board.player: board.addInput(4, board.cpu)
        elif board.hashBoard[1] == board.player: board.addInput(7, board.cpu)
        elif board.hashBoard[7] == board.player: board.addInput(2, board.cpu)
        elif board.hashBoard[3] == board.player: board.addInput(5, board.cpu)
        elif board.hashBoard[5] == board.player: board.addInput(3, board.cpu)
        
        self.firstTrun = False