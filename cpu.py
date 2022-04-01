
class CPU:
    def __init__(self):
        self.firstTrun = True

    def pickMove(self, board):
        if self.firstTrun == True: self.turn1(board)
        else:
            cWinSoon = self.checkForWin(board, board.player, board.cpu)
            if cWinSoon[0] == True:
                    
                board.addInput(cWinSoon[1], board.cpu)
            else:
                pWinSoon = self.checkForWin(board, board.cpu, board.player)
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
                        
                    elif board.hashBoard[0] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[8] == board.player and board.hashBoard[3] == ' ': board.addInput(3, board.cpu)
                    elif board.hashBoard[0] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[8] == board.player and board.hashBoard[1] == ' ': board.addInput(1, board.cpu)
                    elif board.hashBoard[0] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[8] == board.player and board.hashBoard[5] == ' ': board.addInput(5, board.cpu)
                    elif board.hashBoard[0] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[8] == board.player and board.hashBoard[7] == ' ': board.addInput(7, board.cpu)

                    elif board.hashBoard[2] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[6] == board.player and board.hashBoard[3] == ' ': board.addInput(3, board.cpu)
                    elif board.hashBoard[2] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[6] == board.player and board.hashBoard[1] == ' ': board.addInput(1, board.cpu)
                    elif board.hashBoard[2] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[6] == board.player and board.hashBoard[5] == ' ': board.addInput(5, board.cpu)
                    elif board.hashBoard[2] == board.player and board.hashBoard[4] == board.cpu and board.hashBoard[6] == board.player and board.hashBoard[7] == ' ': board.addInput(7, board.cpu)
                        
                    else:
                        for i, _ in enumerate(board.hashBoard):
                            if _ == ' ':
                                board.addInput(i, board.cpu)
                                break

    def checkForWin(self, board, oMark, sMark):

        ## Horizontal
        if board.hashBoard[0] == board.hashBoard[1] and board.hashBoard[0] == sMark:
            if board.hashBoard[2] != oMark:
                return True, 2
        if board.hashBoard[3] == board.hashBoard[4] and board.hashBoard[3] == sMark:
            if board.hashBoard[5] != oMark:
                return True, 5
        if board.hashBoard[6] == board.hashBoard[7] and board.hashBoard[6] == sMark:
            if board.hashBoard[8] != oMark:
                return True, 8

        ## Horizontal Inverse
        if board.hashBoard[2] == board.hashBoard[1] and board.hashBoard[2] == sMark:
            if board.hashBoard[0] != oMark:
                return True, 0
        if board.hashBoard[5] == board.hashBoard[4] and board.hashBoard[5] == sMark:
            if board.hashBoard[3] != oMark:
                return True, 3
        if board.hashBoard[8] == board.hashBoard[7] and board.hashBoard[8] == sMark:
            if board.hashBoard[6] != oMark:
                return True, 6

        ## Horizontal Middle
        if board.hashBoard[0] == board.hashBoard[2] and board.hashBoard[0] == sMark:
            if board.hashBoard[1] != oMark:
                return True, 1
        if board.hashBoard[3] == board.hashBoard[5] and board.hashBoard[3] == sMark:
            if board.hashBoard[4] != oMark:
                return True, 4
        if board.hashBoard[6] == board.hashBoard[8] and board.hashBoard[6] == sMark:
            if board.hashBoard[7] != oMark:
                return True, 7

        ## Vertical
        if board.hashBoard[0] == board.hashBoard[3] and board.hashBoard[0] == sMark:
            if board.hashBoard[6] != oMark:
                return True, 6
        if board.hashBoard[1] == board.hashBoard[4] and board.hashBoard[1] == sMark:
            if board.hashBoard[7] != oMark:
                return True, 7
        if board.hashBoard[2] == board.hashBoard[5] and board.hashBoard[2] == sMark:
            if board.hashBoard[8] != oMark:
                return True, 8

        ## Vertical Inverse
        if board.hashBoard[6] == board.hashBoard[3] and board.hashBoard[6] == sMark:
            if board.hashBoard[0] != oMark:
                return True, 0
        if board.hashBoard[7] == board.hashBoard[4] and board.hashBoard[7] == sMark:
            if board.hashBoard[1] != oMark:
                return True, 1
        if board.hashBoard[8] == board.hashBoard[5] and board.hashBoard[8] == sMark:
            if board.hashBoard[2] != oMark:
                return True, 2
                
        ## Vertical Middle
        if board.hashBoard[0] == board.hashBoard[6] and board.hashBoard[0] == sMark:
            if board.hashBoard[3] != oMark:
                return True, 3
        if board.hashBoard[1] == board.hashBoard[7] and board.hashBoard[1] == sMark:
            if board.hashBoard[4] != oMark:
                return True, 4
        if board.hashBoard[2] == board.hashBoard[8] and board.hashBoard[2] == sMark:
            if board.hashBoard[5] != oMark:
                return True, 5

        ## Diagonal
        if board.hashBoard[0] == board.hashBoard[4] and board.hashBoard[0] == sMark:
            if board.hashBoard[8] != oMark:
                return True, 8
        if board.hashBoard[2] == board.hashBoard[4] and board.hashBoard[2] == sMark:
            if board.hashBoard[6] != oMark:            
                return True, 6

        ## Diagonal Inverse
        if board.hashBoard[8] == board.hashBoard[4] and board.hashBoard[8] == sMark:
            if board.hashBoard[0] != oMark:
                return True, 0
        if board.hashBoard[6] == board.hashBoard[4] and board.hashBoard[6] == sMark:
            if board.hashBoard[2] != oMark:            
                return True, 2

        ## Diagonal Middle
        if board.hashBoard[0] == board.hashBoard[8] and board.hashBoard[0] == sMark:
            if board.hashBoard[4] != oMark:
                return True, 4
        if board.hashBoard[2] == board.hashBoard[6] and board.hashBoard[2] == sMark:
            if board.hashBoard[4] != oMark:            
                return True, 4

        return False, ''
        
            
    def turn1(self, board):
        if board.hashBoard[4] == board.player: board.addInput(0, board.cpu)
        elif board.hashBoard[0] == board.player or board.hashBoard[2] == board.player or board.hashBoard[6] == board.player or board.hashBoard[8] == board.player: board.addInput(4, board.cpu)
        elif board.hashBoard[1] == board.player: board.addInput(0, board.cpu)
        elif board.hashBoard[7] == board.player: board.addInput(6, board.cpu)
        elif board.hashBoard[3] == board.player: board.addInput(0, board.cpu)
        elif board.hashBoard[5] == board.player: board.addInput(2, board.cpu)
        
        self.firstTrun = False