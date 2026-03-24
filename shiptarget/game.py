import pgzrun, random, itertools, time

WIDTH = 400
HEIGHT = 400

speed = 1

ship = Actor("ship")
block = Actor("block")

blockpos = [(50, 50), (50, 350), (350, 350), (350, 50)]
blockposition = itertools.cycle(blockpos)

starttime = time.time()

def game_end():
    print("Game Over")
    total = round(time.time() - starttime, 2)
    print("Time: ", total, "s")
    print("Ticks: ", total / speed)
    exit()

def update():
    if time.time() - starttime > 1:
        if ship.colliderect(block):
            game_end()

def draw():
    screen.clear()
    ship.draw()
    block.draw()

def move_block():
    animate(block, "bounce_end", duration=speed, pos=next(blockposition), on_finished=move_block)

def next_ship_target():
    ship.target = (random.randint(50, 350), random.randint(50, 350))
    target_angle = ship.angle_to(ship.target)
    ship.angle = target_angle
    animate(ship, "linear", duration=speed, pos=ship.target, on_finished=next_ship_target)

move_block()
next_ship_target()

pgzrun.go()