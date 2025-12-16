import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    for i in range(100, 300, 10):
        rect = Rect((i, (400-i)), (i*2, (400-i)*2))
        screen.draw.rect(rect, "pink")

pgzrun.go()