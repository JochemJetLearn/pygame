import pgzrun, random

WIDTH = 800
HEIGHT = 600

rats = [Actor("rat.png"), Actor("rat.png"), Actor("rat.png")]
for i in rats:
    i.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
shown_rats = []
lines = []

debug_points = False

last_rat = None

def draw():
    screen.blit("bg.png", (0, 0))
    if debug_points:
        for i in rats:
            screen.draw.filled_circle(i.pos, 20, "red")
    for i in shown_rats:
        i.draw()
    for i in lines:
        screen.draw.line(i[0], i[1], "white")

def on_mouse_down(pos):
    global last_rat
    for i in rats:
        if i.collidepoint(pos):
            shown_rats.append(i)
            rats.remove(i)
            if last_rat != None:
                lines.append((last_rat.pos, i.pos))
            last_rat = i

pgzrun.go()