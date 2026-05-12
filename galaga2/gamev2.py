import pgzrun, time, pygame

WIDTH = 500
HEIGHT = 750

shipspeed = 5
bulletsspeed = 5
bugspeed = 1

score = 0

ship = Actor('ship')
ship.pos = (WIDTH // 2, HEIGHT - 50)

lose = False
win = False

starttime = time.time()
endtime = 0

bugs = []
bullets = []

def reset():
    global score, lose, win, starttime, bugs, bullets, WIDTH, HEIGHT, height
    starttime = time.time()
    if win:
        WIDTH += 100
    if lose:
        score = 0
        WIDTH = 500
        HEIGHT = 750
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    bugs = []
    bullets = []
    display_bugs()
    lose = False
    win = False
    

def display_bugs():
    for x in range(WIDTH // 100):
        for y in range(5):
            bug = Actor("enemy.png")
            bug.pos = (50+x*100, 50+y*75)
            bugs.append(bug)

def update():
    global score, lose, win, endtime
    if lose or win:
        return
    if keyboard.left and 50 < ship.x:
        ship.x -= shipspeed
    if keyboard.right and ship.x < WIDTH-50:
        ship.x += shipspeed

    if len(bugs) == 0:
        win = True
        endtime = time.time()
    
    for i in bugs:
        i.y += 1
        if i.y > HEIGHT-75:
            lose = True

    for bullet in bullets:
        bullet.y -= bulletsspeed
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
        screen.draw.text(f"Game Over, Score: {score}, Level {WIDTH // 100-4}", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="red")
        screen.draw.text(f"Press R to reset", center=(WIDTH//2, HEIGHT//2+100), fontsize=50, color="red")
        return
    if win:
        screen.draw.text(f"You Win! Time: {round(endtime-starttime, 2)}s, Level {WIDTH // 100-4} ({score} Pt.)", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="green")
        screen.draw.text(f"Press R to play the next level", center=(WIDTH//2, HEIGHT//2+100), fontsize=50, color="green")
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
    if key == keys.R and (lose or win):
        reset()

pgzrun.go()