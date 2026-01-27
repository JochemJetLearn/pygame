import pgzrun, random

HEIGHT = 800
WIDTH = 1000

plastic = ["battery.png", "chips_bag.png", "plastic_bag.png", "plastic_bottle.png"]

items = []

current_level = 1
final_level = 6

start_speed = 12

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
    return new_items

def update(): # checks if there are no items left
    global items
    if len(items) == 0:
        items = make_items(current_level)

def draw():
    global plastic, items
    screen.clear()
    screen.blit("background.png", (0, 0))
    for i in items:
        i.draw()

pgzrun.go()