import pgzrun

WIDTH = 800
HEIGHT = 500

ball = Actor("ball.png")
ball.pos = (50, 250)

def animation():
    animate(ball, pos=(750, 250), duration=3)

def draw():
    screen.fill("light blue")
    screen.blit("grass.png", (0, 0))
    ball.draw()

animation()

pgzrun.go()