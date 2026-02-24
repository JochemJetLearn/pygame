import pgzrun, random

WIDTH = 1080
HEIGHT = 750

score = 0
speed = 2

game_over = False

apple = Actor("apple.png")
apple.pos = (540, 50)

basket = Actor("basket.png")
basket.pos = (540, 700)

def place_apple():
    apple.y = 50
    apple.x = random.randint(150, WIDTH-150)

def update():
    global speed, score, game_over
    if game_over:
        return
    if keyboard.left:
        basket.x -= speed
    if keyboard.right:
        basket.x += speed
    apple.y += speed
    if apple.y > HEIGHT-80:
        if basket.colliderect(apple):
            speed += 0.5
            score += 1
            place_apple()
        else:
            game_over = True

def draw():
    screen.fill("light blue")
    screen.blit("grass.png", (0,0))
    screen.blit("tree.png", (0,0))
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="black")
    apple.draw()
    basket.draw()
    if game_over:
        screen.draw.text(f"Game Over!\nScore {score}", center=(WIDTH/2, HEIGHT/2), fontsize=100, color="red")

pgzrun.go()