from ezgraphics import GraphicsWindow

win = GraphicsWindow(750, 750)
canvas = win.canvas()

canvas.setBackground('black')

canvas.setColor('white')
canvas.drawOval(canvas.width() / 2.0 - 100, canvas.height() / 2.0 + 100, 200, 200)
canvas.drawOval(canvas.width() / 2.0 - 70, canvas.height() / 2.0 - 30, 140, 140)
canvas.drawOval(canvas.width() / 2.0 - 40, canvas.height() / 2.0 - 100, 80, 80)

win.wait()

"""
Terminal> python3 snowman.py

"""