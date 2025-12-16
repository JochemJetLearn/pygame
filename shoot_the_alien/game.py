import pgzrun, random, time

WIDTH = 500
HEIGHT = 500

TITLE = "Super Sniper"

alien = Actor("alien.png")
alien.x = 250
alien.y = 250
hit = False
miss = False
last = None
stats = {
    "hit": 0,
    "miss": 0,
    "times": []
}
def draw():
    global hit, miss, last, stats
    screen.clear()
    screen.fill("light blue")
    alien.draw()
    if hit:
        if last == None:
            last = time.time()
        else:
            current = time.time()
            stats["hit"] += 1
            stats["times"].append(current-last)
            screen.draw.text(f"Target Hit!\nTime: {round(current-last, 2)}", (390, 20), color="black")
            last = current
        hit = False
    elif miss:
        if last != None:
            current = time.time()
            last -= 1
            stats["miss"] += 1
            screen.draw.text(f"miss (+1s)\nTime: {round(current-last, 2)}", (390, 20), color="black")
        miss = False
    if stats["hit"] > 0:
        avg = 0
        for i in stats["times"]:
            avg += i
        avg /= stats["hit"]
        screen.draw.text(f"Stats:\nhit: {stats['hit']}\nmissed: {stats['miss']}\navg miss/hit: {round(stats['miss']/stats['hit'], 2)}\navg time/hit: {round(avg, 2)}s", (20, 20), color="black")

def on_mouse_down(pos):
    global hit
    global miss
    if alien.collidepoint(pos):
        alien.x = random.randint(50, 450)
        alien.y = random.randint(50, 450)
        hit = True
    else:
        miss = True

pgzrun.go()

if stats["hit"] == 0:
    pgzrun.os._exit(0)

avg = 0
for i in stats["times"]:
    avg += i
avg /= stats["hit"]

print(f"ended game, stats:\nhit: {stats['hit']}\nmissed: {stats['miss']}\navg miss/hit: {round(stats['miss']/stats['hit'], 2)}\navg time/hit: {round(avg, 2)}s")