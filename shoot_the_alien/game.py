import pgzrun, random

WIDTH = 500
HEIGHT = 500

TITLE = "Super Sniper"

alien = Actor("alien.png")

def draw():
    screen.clear()
    screen.fill("light blue")
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.x = random.randint(50, 450)
        alien.y = random.randint(50, 450)

pgzrun.go()