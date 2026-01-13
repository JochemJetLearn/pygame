import random, pgzrun, time

WIDTH = 800
HEIGHT = 600

sattalites = []
satt_num = 8

lines = []

clicked_num = 0

start_time = time.time()
end_time = False

def create_sattalites():
    for i in range(satt_num):
        sattalite = Actor('sattalite')
        sattalite.pos = (random.randint(50, 750), random.randint(50, 550))
        sattalites.append(sattalite)

def draw():
    screen.clear()
    screen.blit("galaxy", (0, 0))
    for num in range(1, len(sattalites)+1):
        sattalites[num-1].draw()
        screen.draw.text(str(num), (sattalites[num-1].x, sattalites[num-1].y+15), color="white")
    for i in lines:
        screen.draw.line(i[0], i[1], "white")
    if end_time != False:
        total = end_time - start_time
        screen.draw.text(f"Run completed in {round(total, 2)} seconds!", (25, 25), color="white")

def on_mouse_down(pos):
    global clicked_num, lines, end_time
    if clicked_num < satt_num:
        if sattalites[clicked_num].collidepoint(pos):
            if clicked_num:
                lines.append((sattalites[clicked_num].pos, sattalites[clicked_num-1].pos))
            clicked_num += 1
        else:
            lines = []
            clicked_num = 0
    if clicked_num == satt_num:
        end_time = time.time()

create_sattalites()

pgzrun.go()
