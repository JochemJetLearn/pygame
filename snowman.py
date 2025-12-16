import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.filled_circle((300, 500), 100, "white")
    screen.draw.filled_circle((300, 310), 90, "white")
    screen.draw.filled_circle((300, 145), 75, "white")
    screen.draw.line((250, 160), (250, 175), "red")
    screen.draw.line((350, 160), (350, 175), "red")
    screen.draw.line((250, 175), (350, 175), "red")
    screen.draw.filled_circle((270, 130), 10, "black")
    screen.draw.filled_circle((330, 130), 10, "black")
    screen.draw.filled_circle((300, 250), 8, "black")
    screen.draw.filled_circle((300, 270), 8, "black")
    screen.draw.filled_circle((300, 290), 8, "black")
    screen.draw.filled_circle((300, 310), 8, "black")
    rect = Rect((300, 220), (100, 35))
    rect.center = (300, 220)
    screen.draw.filled_rect(rect, "orange")

pgzrun.go()