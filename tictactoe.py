class tictac:

    def __init__(self):
        self.board = [[ '-','-','-'] ,[ '-','-','-'],[ '-','-','-']]
        self.tokenNumber = 0


    def insert(self,row,col, token):
        # if token  not in ['X','O']:
        #     return
        # if self.board[row][col] != '-' :
        #     return
        self.board[row][col] = token
        self.tokenNumber+=1

    def printboard(self):
        if not self.board:
            return
        for i in range(len(self.board)):
            row = self.board[i]
            string = ""
            for index in range(len(row)):
                string += str(row[index]) +'|'
            print string[:-1]

    def isFull(self):
        return self.tokenNumber == 9

    def ai(self):
        if self.isFull():
            raise Exception("no legal space")

        for rowIndex, row in enumerate(self.board):
            for colIndex,token in enumerate(row):
                if token == '-':
                    self.insert(rowIndex, colIndex, 'O')
                    return


board = tictac();
board.insert(0,1,'X');
board.printboard();
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()
board.printboard()
board.ai()

# print board.board