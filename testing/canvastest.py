import ezgraphics as ez

win = ez.GraphicsWindow(600, 600)
canvas = win.canvas()

w = canvas.width()
h = canvas.height()
w1 = canvas.width() / 3.0
w2 = canvas.width() * 2.0 / 3.0
h1 = canvas.height() / 3.0
h2 = canvas.height() * 2.0 / 3.0

s = [(25, 25), (225, 25), (425, 25), (25, 225), (225, 225), (425, 225), (25, 425), (225, 425), (425, 425)]

canvas.drawLine(w1, 0, w1, h)
canvas.drawLine(w2, 0, w2, h)
canvas.drawLine(0, h1, w, h1)
canvas.drawLine(0, h2, w, h2)

turn = 0
player = True

def circle(coords):
    x, y = coords
    canvas.drawOval(x, y, 150, 150)

def cross(coords):
    x, y = coords
    canvas.drawLine(x, y, x+150, y+150)
    canvas.drawLine(x, y+150, x+150, y)

def won(board):
    possible = ['X', 'O']

    for i in range(3):
        for j in range(2):
            if board[i] == board[i+3] == board[i+6] == possible[j]:
                return True
        
    for i in range(0, 7, 3):
        for j in range(2):
            if board[i] == board[i+1] == board[i+2] == possible[j]:
                return True
    
    for j in range(2):
        if board[0] == board[4] == board[8] == possible[j]:
            return True
        elif board[2] == board[4] == board[6] == possible[j]:
            return True
        else:
            return False

def busy(board, pos):
    if board[pos] != '':
        return True
    else:
        return False

def markBoard(board, pos, player, turn):
    taken = busy(board, pos)
    
    if not taken:
        if player:
            cross(s[pos])
            board[pos] = 'X'
        else:
            circle(s[pos])
            board[pos] = 'O'
        
        turn += 1
        return board, turn
    else:
        print('That square is taken!')
        play(turn, player)

def play(turn, player):
    board = ['' for i in range(9)]
    
    game = True

    while game:
        x, y = win.getMouse()

        if turn % 2 == 0:
            player = True
        else:
            player = False

        if x < w1 and y < h1:
            board, turn = markBoard(board, 0, player, turn)
        elif w1 < x < w2 and y < h1:
            board, turn = markBoard(board, 1, player, turn)
        elif w2 < x and y < h1:
            board, turn = markBoard(board, 2, player, turn)
        elif x < w1 and h1 < y < h2:
            board, turn = markBoard(board, 3, player, turn)
        elif w1 < x < w2 and h1 < y < h2:
            board, turn = markBoard(board, 4, player, turn)
        elif w2 < x and h1 < y < h2:
            board, turn = markBoard(board, 5, player, turn)
        elif x < w1 and h2 < y:
            board, turn = markBoard(board, 6, player, turn)
        elif w1 < x < w2 and h2 < y:
            board, turn = markBoard(board, 7, player, turn)
        elif w2 < x and h2 < y:
            board, turn = markBoard(board, 8, player, turn)
        else:
            pass

        winner = won(board)

        if winner and player:
            print('Player 1 is the winner!')
            game = False
        elif winner and not player:
            print('Player 2 is the winner!')
            game = False

play(turn, player)

win.wait()