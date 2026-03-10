import pgzrun

WIDTH = 400
HEIGHT = 400

box = Rect(200, 200, 50, 50)
x = 200
y = 200
color = "white"

margin = 50

def update():
    global box, color, x, y, margin
    box.center = (x, y)
    if x < margin:
        color = "red"
    elif x > WIDTH - margin:
        color = "blue"
    elif y < margin:
        color = "green"
    elif y > HEIGHT - margin:
        color = "yellow"
    else:
        color = "white"

def draw():
    screen.fill("black")
    screen.draw.filled_rect(box, color)

def on_key_down(key):
    global color, x, y
    if key == keys.UP:
        y -= 10
    elif key == keys.DOWN:
        y += 10
    elif key == keys.LEFT:
        x -= 10
    elif key == keys.RIGHT:
        x += 10

pgzrun.go()