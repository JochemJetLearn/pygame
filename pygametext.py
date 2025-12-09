import pgzrun, random

def draw():
    screen.clear()
    screen.draw.text("red", (150, 100), color="red")
    screen.draw.text("blue", (150, 250), color="blue")
    screen.draw.text("green", (150, 400), color="green")
    screen.draw.text("purple", (300, 100), color="purple")
    screen.draw.text("orange", (300, 250), color="orange")
    screen.draw.text("yellow", (300, 400), color="yellow")
    screen.draw.text("lightblue", (450, 100), color="lightblue")
    screen.draw.text("#e13785", (450, 250), color="#e13785")
    screen.draw.text("magenta", (450, 400), color="magenta")

pgzrun.go()