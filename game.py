import pgzrun, random, time

WIDTH = 512
HEIGHT = 512

enemy_files = ["blue_enemy.png", "green_enemy.png", "red_enemy.png", "white_enemy.png"]
ship = Actor("ship.png")
ship.pos = (WIDTH / 2, HEIGHT / 2)
explosion_frames = ["explosion1.png", "explosion2.png", "explosion3.png", "explosion4.png", "explosion5.png", "explosion6.png"]
distance = 50
running = True

win_score = 30

explosions = []
health = 4
score = 0
enemys = []
last_enemy = time.time()

def hit(enemy):
    global health
    health -= 1
    enemys.remove(enemy)

def death(enemy):
    global score
    score += 1
    enemys.remove(enemy)
    explosions.append([enemy.pos, time.time()])

def spawn_enemy():
    global last_enemy
    index = random.randint(0, len(enemy_files) - 1)
    enemy = Actor(enemy_files[index])
    enemys.append(enemy)
    if index == 0:
        enemy.pos = (WIDTH, 0)
    elif index == 1:
        enemy.pos = (0, 0)
    elif index == 2:
        enemy.pos = (0, HEIGHT)
    elif index == 3:
        enemy.pos = (WIDTH, HEIGHT)
    animate(enemy, "linear", duration=5, pos=(WIDTH/2, HEIGHT/2))
    last_enemy = time.time()

def update():
    global running
    if not running:
        return
    if score >= win_score:
        running = False
        return
    for enemy in enemys:
        if ship.colliderect(enemy):
            death(enemy)
        pos = enemy.pos
        if pos[0] > WIDTH/2-distance and pos[0] < WIDTH/2+distance and pos[1] > HEIGHT/2-distance and pos[1] < HEIGHT/2+distance:
            hit(enemy)
    if time.time() - last_enemy > 1:
        spawn_enemy()
    if health <= 0:
        running = False

def draw():
    screen.blit("map.png", (0, 0))
    for i in explosions:
        curr_time = time.time() - i[1]
        if curr_time > 0.5:
            explosions.remove(i)
        else:
            frame = int(curr_time / 0.5 * len(explosion_frames))
            screen.blit(explosion_frames[frame], i[0])
        
    if running:
        for enemy in enemys:
            enemy.draw()
        ship.draw()
        screen.draw.text("Health: " + str(health), (10, 10), color="black")
        screen.draw.text("Score: " + str(score), (10, 30), color="black")
    else:
        if score >= win_score:
            screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="green")
        else:
            screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")
            screen.draw.text("Score: " + str(score), center=(WIDTH/2, HEIGHT/2 + 50), fontsize=30, color="black")

def on_mouse_down(pos):
    animate(ship, "bounce_end", duration=0.5, pos=pos)
    ship.angle = ship.angle_to(pos) - 90

pgzrun.go()