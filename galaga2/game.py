import pgzrun, time

WIDTH = 500
HEIGHT = 750

score = 0

ship = Actor('ship')
ship.pos = (WIDTH // 2, HEIGHT - 50)

lose = False
win = False

starttime = time.time()
endtime = 0

bugs = []
bullets = []

def display_bugs():
    for x in range(WIDTH // 100):
        for y in range(5):
            bug = Actor("enemy.png")
            bug.pos = (50+x*100, 50+y*75)
            bugs.append(bug)

def update():
    global score, lose, win
    if lose or win:
        return
    if keyboard.left and 50 < ship.x:
        ship.x -= 5
    if keyboard.right and ship.x < WIDTH-50:
        ship.x += 5

    if len(bugs) == 0:
        win = True
    
    for i in bugs:
        i.y += 1
        if i.y > HEIGHT-75:
            lose = True

    for bullet in bullets:
        bullet.y -= 5
        for i in bugs:
            if i.colliderect(bullet):
                try:
                    bugs.remove(i) 
                    bullets.remove(bullet)
                    score += 1
                except ValueError:
                    pass

display_bugs()

def draw():
    global lose, win, score
    screen.clear()
    ship.draw()
    if lose:
        screen.draw.text(f"Game Over, Score: {score}", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="red")
        return
    if win:
        screen.draw.text(f"You Win!", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="green")
        return
    for i in bugs:
        i.draw()
    for i in bullets:
        i.draw()

def on_key_down(key):
    global score
    if key == keys.SPACE:
        bullet = Actor("bullet.png")
        bullet.pos = (ship.x, HEIGHT - 50)
        bullets.append(bullet)

pgzrun.go()