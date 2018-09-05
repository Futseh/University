import ezgraphics as ez

win = ez.GraphicsWindow(600, 600)
canvas = win.canvas()

def circle(coords):
    x, y = coords
    canvas.drawOval(x, y, 150, 150)

def cross(coords):
    x, y = coords
    canvas.drawLine(x, y, x+150, y+150)
    canvas.drawLine(x, y+150, x+150, y)

def won(X, O):
    for i in range(3):
        if X[i] == X[i+3] == X[i+6] == True or O[i] == O[i+3] == O[i+6] == True:
            return True
        
    for i in range(0, 7, 3):    
        if X[i] == X[i+1] == X[i+2] == True or O[i] == O[i+1 == O[i+2] == True:
            return True
    
    if X[0] == X[4] == X[8] == True or O[0] == O[4] == O[8] == True:
        return True
    elif X[2] == X[4] == X[6] == True or O[2] == O[4] == O[6] == True:
        return True
    else:
        return False


def busy(pos):
    if X[pos] or O[pos]:
        return True
    else:
        return False

def play():
    pass

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

X = [False for i in range(9)]
O = [False for i in range(9)]

while True:
    x, y = win.getMouse()

    if turn % 2 == 0:
        cros = True
        turn += 1
    else:
        cros = False
        turn += 1

    if x < w1 and y < h1:
        if cros:
            cross(s[0])
        else:
            circle(s[0])

win.wait()