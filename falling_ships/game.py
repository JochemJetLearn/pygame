import pgzrun, random

WIDTH = 1200
HEIGHT = 600

win = False
lose = False

zuko = Actor("zuko.png")
zuko.pos = (WIDTH//2, HEIGHT - 50)

ships = []
bullets = []

def place_ships():
    for i in range(10):
        ship = Actor("ship.png")
        ship.pos = (i*WIDTH//10+WIDTH//20, WIDTH//20)
        ships.append(ship)

place_ships()

def update():
    global win, lose
    if win or lose:
        return
    if keyboard.left and zuko.left > 0:
        zuko.x -= 5
    if keyboard.right and zuko.right < WIDTH:
        zuko.x += 5
    for i in ships:
        i.y += 1
        if i.y > HEIGHT-75:
            lose = True
            return
    for i in bullets:
        i.y -= 5
        if i.y < 0:
            bullets.remove(i)
        for j in ships:
            if i.colliderect(j):
                ships.remove(j)
                bullets.remove(i)
                break
    if len(ships) == 0:
        win = True

def draw():
    if not (win or lose):
        screen.blit("bg.png", (0, 0))
        zuko.draw()
        for i in ships:
            i.draw()
        for i in bullets:
            i.draw()
    elif win:
        screen.fill((0, 255, 0))
        screen.draw.text("You Win!", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="black")
    elif lose:
        screen.fill((255, 0, 0))
        screen.draw.text("You Lose!", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="black")

def shoot():
    bullet = Actor("bullet.png")
    bullet.pos = (zuko.x, zuko.y - 20)
    bullets.append(bullet)

def on_key_down(key):
    if key == keys.SPACE:
        shoot()

pgzrun.go()