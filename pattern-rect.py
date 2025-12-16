import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    w = WIDTH
    h = HEIGHT-400
    for i in range(20):
        rect = Rect((0, 0), (w, h))
        rect.center = (300, 300)
        screen.draw.rect(rect, "purple")
        w -= 20
        h += 20

pgzrun.go()