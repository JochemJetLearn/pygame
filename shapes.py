import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    screen.fill("lightblue")
    rect = Rect((100, 100), (100, 100))
    screen.draw.rect(rect, "red")
    rect2 = Rect((300, 300), (150, 150))
    screen.draw.filled_rect(rect2, "blue")
    screen.draw.line((200, 250), (450 ,200), "black")
    screen.draw.line((100, 400), (300 ,400), "black")
    screen.draw.line((300, 400), (200 ,200), "black")
    screen.draw.line((200, 200), (100 ,400), "black")
    screen.draw.circle((300, 100), 50, "darkgreen")
    screen.draw.filled_circle((400, 100), 50, "darkgreen")
    rect3 = Rect((100, 400), (200, 100))
    screen.draw.filled_rect(rect3, "yellow")

pgzrun.go()