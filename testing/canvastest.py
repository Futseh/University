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
    elif w1 < x < w2 and y < h1:
        if cros:
            cross(s[1])
        else:
            circle(s[1])
    elif w2 < x and y < h1:
        if cros:
            cross(s[2])
        else:
            circle(s[2])
    elif x < w1 and h1 < y < h2:
        if cros:
            cross(s[3])
        else:
            circle(s[3])
    elif w1 < x < w2 and h1 < y < h2:
        if cros:
            cross(s[4])
        else:
            circle(s[4])
    elif w2 < x and h1 < y < h2:
        if cros:
            cross(s[5])
        else:
            circle(s[5])
    elif x < w1 and h2 < y:
        if cros:
            cross(s[6])
        else:
            circle(s[6])
    elif w1 < x < w2 and h2 < y:
        if cros:
            cross(s[7])
        else:
            circle(s[7])
    elif w2 < x and h2 < y:
        if cros:
            cross(s[8])
        else:
            circle(s[8])
    else:
        pass

win.wait()