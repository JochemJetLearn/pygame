import pgzrun, random

HEIGHT = 850
WIDTH = 1200

horses = []

animations = []

current_level = 1
total_levels = 8
speed = 10
speed_increase = 1.1

win = False
game_over = False
start = False

bet = random.randint(0, current_level)

TITLE = "Click to start the game!"

def create_horses(lvl):
    global horses
    gaps = lvl + 2
    gap_size = HEIGHT / gaps
    nums = list(range(1, lvl+2))
    random.shuffle(nums)
    for i in range(len(nums)):
        horse = Actor("horse.png")
        horse.pos = (100, (i+1) * gap_size)
        horses.append(horse)

def next_round(lvl):
    global horses, animations, speed, win, TITLE, current_level, bet
    if lvl == total_levels:
        win = True
    else:
        current_level += 1
        bet = random.randint(0, current_level)
    stop_animations()
    speed -= speed_increase
    horses = []
    TITLE = "Horse Bet: " + str(bet+1) + ", Level: " + str(current_level)
    

def animate_horses():
    global animations
    for i in horses:
        animation = animate(i, duration=speed, x=WIDTH, on_finished=handle_game_over)
        animations.append(animation)

def place_horses(lvl):
    create_horses(lvl)
    animate_horses()

def stop_animations():
    global animations
    for i in animations:
        if i.running:
            i.stop()
    animations = []

def handle_game_over():
    global horses, animations, game_over
    game_over = True
    stop_animations()
    horses = []

def update():
    global horses, current_level
    if len(horses) == 0 and (not game_over and not win) and start:
        place_horses(current_level)

def draw():
    screen.blit("sand.jpg", (0, 0))
    if win:
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=100, color="black")
    elif game_over:
        screen.draw.text("Game Over!", center=(WIDTH/2, HEIGHT/2), fontsize=100, color="red")
    elif not start:
        screen.draw.text(TITLE, center=(WIDTH/2, HEIGHT/2), fontsize=50, color="black")
    elif start:
        screen.draw.text(str(bet+1), (50, HEIGHT/2), color="black", fontsize=50)
        for i in range(len(horses)):
            horses[i].draw()
            screen.draw.text(str(i+1), (horses[i].x, horses[i].y+30), color="black")

def on_mouse_down(pos):
    global bet, TITLE, start
    if not start:
        start = True
        TITLE = "Level: " + str(current_level)
    if not game_over and not win and start:
        for i in range(len(horses)):
            if horses[i].collidepoint(pos):
                if i == bet:
                    next_round(current_level)
                    break
                else:
                    handle_game_over()
                    break
pgzrun.go()