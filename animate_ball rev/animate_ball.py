import pgzrun

WIDTH = 800
HEIGHT = 500

ball = Actor("ball.png")
ball.pos = (50, 250)

round = 0
finish = 10

def animation():
    global round
    round += 1
    animate(ball, pos=(750, 250), duration=3, on_finished=animation_reverse)

def animation_reverse():
    global round
    if round == finish:
        animate(ball, pos=(50, 250), duration=3)
    else:
        animate(ball, pos=(50, 250), duration=3, on_finished=animation)

def draw():
    screen.fill("light blue")
    screen.blit("grass.png", (0, 0))
    ball.draw()

def on_key_down(key):
    if key == keys.SPACE:
        animation()

pgzrun.go()