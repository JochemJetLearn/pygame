import pgzrun, random, time

WIDTH = 800
HEIGHT = 600

lose = False
death_time = 0

score = 0

player = Actor("robo.png")
player.pos = (WIDTH // 2, HEIGHT // 2)

coin = Actor("coin.png")
coin.pos = (random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))

bomb = Actor("bomb.png")
bomb.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

def update():
    global score, lose, death_time
    if lose:
        if time.time() - death_time > 2:
            score = 0
            lose = False
            bomb.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            player.pos = (WIDTH // 2, HEIGHT // 2)
            coin.pos = (random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
        return
    if keyboard.left and player.left > 0:
        player.x -= 5
        player.image = "robo-left.png"
    if keyboard.right and player.right < WIDTH:
        player.x += 5
        player.image = "robo-right.png"
    if keyboard.up and player.top > 0:
        player.y -= 5
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 5
    if not (keyboard.left or keyboard.right):
        player.image = "robo.png"
    if player.colliderect(coin):
        coin_placed = False
        while not coin_placed:
            coin.pos = (random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
            if not coin.colliderect(player) and not coin.colliderect(bomb):
                coin_placed = True
        score += 1
    if player.colliderect(bomb):
        lose = True
        death_time = time.time()

def draw():
    global score, lose
    screen.blit("bg.png", (0, 0))
    player.draw()
    coin.draw()
    bomb.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=60, color="black")
    if lose:
        screen.draw.text("You lose!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")
        screen.draw.text(f"Score: {score}", center=(WIDTH // 2, HEIGHT // 2+50), fontsize=60, color="black")

pgzrun.go()