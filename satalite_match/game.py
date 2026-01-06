import random, pgzrun, time

WIDTH = 800
HEIGHT = 600

sattalites = []
satt_num = 8

start_time = time.time()

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

def on_mouse_down(pos):

create_sattalites()

pgzrun.go()
