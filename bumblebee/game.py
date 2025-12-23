import pgzrun, random, time

WIDTH = 600
HEIGHT = 500

bee = Actor("bee")
bee.pos = (50, 250)
flower = Actor("flower")
flower.pos = (300, 250)

score = 0
start = time.time()

def draw():
    screen.clear()
    screen.blit("grass", (0, 0))
    bee.draw()
    flower.draw()
    now = time.time()
    screen.draw.text(f"score: {score}", (15, 15))
    if now-start > 60:
        screen.fill("red")
        screen.draw.text(f"Time's up!\nscore: {score}", (300, 250))

def update():
    global score
    if keyboard.left:
        bee.x -= 3
    if keyboard.right:
        bee.x += 3
    if keyboard.up:
        bee.y -= 3
    if keyboard.down:
        bee.y += 3
    
    collected = bee.colliderect(flower)
    if collected:
        score += 1
        flower.pos = (random.randint(50, 550), random.randint(50, 450))

pgzrun.go()