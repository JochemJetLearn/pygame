import pgzrun, random

HEIGHT = 800
WIDTH = 1000

plastic = ["battery.png", "chips_bag.png", "plastic_bag.png", "plastic_bottle.png"]

items = []

animations = []

game_over = False
game_complete = False

current_level = 1
final_level = 6

score = 0

start_speed = final_level*2+1

def get_options_to_create(item_num): # places all items in level into list
    items_to_create = ["paper_bag.png"]
    for i in range(item_num):
        random_option = random.choice(plastic)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create): # creates actor objects for all items
    new_items = []
    for i in items_to_create:
        object = Actor(i)
        new_items.append(object)
    return new_items

def layout_items(items_to_layout): # loads item positions
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for i, j in enumerate(items_to_layout):
        new_x = (i + 1) * gap_size
        j.x = new_x

def make_items(item_num): # makes new items
    items_to_create = get_options_to_create(item_num)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def handle_game_over():
    global game_over
    game_over = True

def handle_game_complete(paperbag):
    global current_level, items, animations, game_complete, score
    stop_animations(animations)
    score += HEIGHT - paperbag.y
    if current_level == final_level:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration = start_speed - current_level*2
        i.anchor = ("center", "bottom")
        animation = animate(i, duration=duration, y=HEIGHT, on_finished=handle_game_over)
        animations.append(animation)

def update(): # checks if there are no items left
    global items
    if len(items) == 0:
        items = make_items(current_level)

def draw():
    global plastic, items, game_over, game_complete, score
    screen.clear()
    screen.blit("background.png", (0, 0))
    screen.draw.text(f"Score: {round(score)}", (10, 10), color="black")
    if game_over:
        screen.draw.text("GAME OVER!!111!!11!", (WIDTH/2, HEIGHT/2), color="red", fontsize=100)
    elif game_complete:
        screen.draw.text("YOU WIN!", (WIDTH/2, HEIGHT/2), color="black", fontsize=100)
    else:
        for i in items:
            i.draw()

def on_mouse_down(pos):
    global items, current_level
    for i in items:
        if i.collidepoint(pos):
            if "paper_bag.png" in i.image:
                handle_game_complete(i)
            else:
                handle_game_over()

pgzrun.go()