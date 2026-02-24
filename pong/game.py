import pgzrun

WIDTH = 800
HEIGHT = 600

gameover = False
score = 0

y = "stop"
x = "stop"

speed = 5
ballspeed = 3

ball = Actor("ball.png")
ball.pos = (400, 200)

bat = Rect((400, 550), (70, 20))

def update():
    global x, y, gameover, score
    if gameover:
        return
    if keyboard.left:
        bat.x -= speed
    if keyboard.right:
        bat.x += speed
    
    if x == "right":
        ball.x += ballspeed
    elif x == "left":
        ball.x -= ballspeed

    if y == "down":
        ball.y += ballspeed
    elif y == "up":
        ball.y -= ballspeed

    if ball.x < 32:
        x = "right"
    if ball.x > WIDTH-32:
        x = "left"
    if ball.y < 32:
        y = "down"
    if ball.colliderect(bat) and y == "down":
        y = "up"
        score += 1
    if ball.y > HEIGHT+32:
        gameover = True

def draw():
    global score, gameover
    screen.fill("black")
    ball.draw()
    screen.draw.filled_rect(bat, "white")
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    if gameover:
        screen.draw.text(f"Game Over!\nScore: {score}", center=(WIDTH/2, HEIGHT/2), fontsize=100, color="red")


def on_key_down(key):
    global x, y
    if x == "stop":
        x = "right"
        y = "down"

pgzrun.go()
