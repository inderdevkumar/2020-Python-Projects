#https://python-forum.io/Thread-Tic-Tac-Toe

from tkinter import *
 
def restart() :
    global isXTurn, isDone, numClicks
    for i in range(3) :
        for j in range(3) :
            grid[i][j].config(text = ' ')  #This is the change. 
            
    numClicks = 0
    isXTurn = True
    isDone = False
    lablStatus.config(text = 'X\'s Turn')
    print(' Game is Restarted')
 
def markSpace(rw, col) :
    global isXTurn, isDone, numClicks
 
    space = grid[rw][col].cget('text')
    if(isDone == True) :
        return
    elif (space == ' ') :
        if (isXTurn) :   #Changed here
            grid[rw][col].config(text = 'X', fg = 'red')
            lablStatus.config(text = 'O\'s Turn')
        else :
            grid[rw][col].config(text = 'O', fg = 'blue')
            lablStatus.config(text = 'X\'s Turn')
    else :
        lablStatus.config(text = 'Invalid Move')
        return
 
    numClicks += 1
    isXTurn = not isXTurn
    gameOver(rw, col)
 
def gameOver(rw, col) :
    global numClicks
    global isDone
    winner = ' '
 
    if(grid[0][0].cget('text')  == grid[1][1].cget('text') and grid[1][1].cget('text') == grid[2][2].cget('text')) :
        winner = grid[0][0].cget('text')
    elif(grid[2][0].cget('text')  == grid[1][1].cget('text') and grid[1][1].cget('text') == grid[0][2].cget('text')) :
        winner = grid[2][0].cget('text')
 
    else :
        for r in range(0, 3) :
            if(grid[r][0].cget('text') != ' ' and grid[r][0].cget('text') == grid[r][1].cget('text') and grid[r][1].cget('text') == grid[r][2].cget('text')):
                winner = grid[r][0].cget('text')
            elif(grid[0][r].cget('text') != ' ' and grid[0][r].cget('text') == grid[1][r].cget('text') and grid[1][r].cget('text') == grid[2][r].cget('text')):
                winner = grid[0][r].cget('text')
 
    isDone = True
    if(winner == ' ' and numClicks >= 9) :
       lablStatus.config(text = 'Tie Game')
    elif(winner != ' ') :
        lablStatus.config(text = winner + ' Wins!')
    else :
        lablStatus.config(text = 'X\'s Turn' if isXTurn else 'O\'s Turn')
        isDone = False
 
grid = [ [ 0 for i in range(3) ] for j in range(3) ]
numClicks = 0
isDone = False
isXTurn = True
 
root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('355x420')
 
topFrame = Frame(root, width = 320, height = 40).place(x = 12, y = 12)
 
lablStatus = Label(topFrame, text = 'O\'s Turn')
lablStatus.config(fg = 'blue', bg = 'yellow', font = 'serif 16 bold')
lablStatus.pack(side = TOP)
 
mainFrame = Frame(root, width = 330, height = 330)
mainFrame.config(bg = 'black')
mainFrame.place(x = 10, y = 42)
 
grid = [ [ 0 for i in range(3) ] for j in range(3) ]
for rw in range(0, 3) :
    for col in range(0, 3) :
        grid[rw][col] =  Button(mainFrame, text=' ', relief = 'solid', command = lambda r = rw, c = col: markSpace(r, c))
        grid[rw][col].config(font = 'monospace 36 bold', fg = 'red', height = 1,  width = 3)
        grid[rw][col].place(x = rw*105 + 10, y=col*105+10)
 
btnRestart = Button(root, text = 'Restart', command = restart, width = 30)
btnRestart.place(x = 45, y = 380)
 
 
root.mainloop()
