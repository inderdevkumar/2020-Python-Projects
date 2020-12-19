
pos_check_for_winnwer = (
    [[(x, y) for y in range(3)] for x in range(3)] + # horizontals winner
    [[(x, y) for x in range(3)] for y in range(3)] + # verticals winner
    [[(d, d) for d in range(3)]] + # diagonal from top-left to bottom-right winner
    [[(2-d, d) for d in range(3)]] # diagonal from top-right to bottom-left winner
)

def whoWonTicTacToe(board):
    
    for positions in pos_check_for_winnwer:
        values = [board[x][y] for (x, y) in positions]
        if (len(set(values)) == 1 and values[0]):
            return values[0]
        
        else:
            return "None of them"
        
board = [["X", "X", "X"],
    ["O", "X", "X"],
    ["O", "X", "O"]]

print(f"{whoWonTicTacToe(board)} is the winner!")
