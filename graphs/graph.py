import pygame, math, tkinter, os, random
from classes import *
from constants import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
camera_pos = [0, 0]
scale = 100
show_ui = True

def tp():
    root = tkinter.Tk()
    root.title("Teleport")
    root.geometry("200x100")
    x_entry = tkinter.Entry(root)
    x_entry.pack()
    y_entry = tkinter.Entry(root)
    y_entry.pack()
    def submit():
        try:
            x = float(x_entry.get())
            y = float(y_entry.get())
            camera_pos[0] = x
            camera_pos[1] = y
            root.destroy()
        except:
            pass
    submit_button = tkinter.Button(root, text="Submit", command=submit)
    submit_button.pack()
    root.mainloop()

def add_graph():
    root = tkinter.Tk()
    root.title("Add Graph")
    root.geometry("300x200")
    func_entry = tkinter.Entry(root)
    func_entry.pack()
    name_entry = tkinter.Entry(root)
    name_entry.pack()
    def submit():
        try:
            func_str = func_entry.get()
            func = eval(f"lambda x, z: {func_str}")
            graph = Graph(func)
            graph.func_str = func_str
            graph.name = name_entry.get() if name_entry.get() != "" else None
            graphs.append(graph)
            root.destroy()
        except Exception as e:
            print(f"Error adding graph: {e}")
    submit_button = tkinter.Button(root, text="Submit", command=submit)
    submit_button.pack()
    root.mainloop()

def draw_graphs():
    size = float_range(camera_pos[0]-WIDTH/scale, camera_pos[0]+WIDTH/scale, 1/scale)
    for graph in graphs:
        graph.draw(screen, camera_pos, scale, size)

def movement(t):
    global scale
    keys = pygame.key.get_pressed()
    speed = 0.25 if keys[pygame.K_LSHIFT] else 1
    if keys[pygame.K_LEFT]:
        camera_pos[0] -= speed / scale * t
    if keys[pygame.K_RIGHT]:
        camera_pos[0] += speed / scale * t
    if keys[pygame.K_UP]:
        camera_pos[1] -= speed / scale * t
    if keys[pygame.K_DOWN]:
        camera_pos[1] += speed / scale * t
    if keys[pygame.K_i]:
        scale *= 1 + 0.1*speed
    if keys[pygame.K_o]:
        scale /= 1 + 0.1*speed

last_click = None
click = False
def mouse_movement():
    global scale, last_click, click
    mouse_pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed(5)
    if pressed[0]:
        if not click:
            click = True
            last_click = mouse_pos
    else:
        click = False
    if pressed[2]:
        scale *= 1.1
    if pressed[1]:
        scale /= 1.1
    if click:
        camera_pos[0] += (last_click[0] - mouse_pos[0]) / scale
        camera_pos[1] += (last_click[1] - mouse_pos[1]) / scale
        last_click = mouse_pos

def buttons():
    mouse = pygame.mouse.get_pos()
    coordinates.text = f"Mouse: {(mouse[0] - WIDTH / 2)/scale + camera_pos[0]:.2f}, {(mouse[1] - HEIGHT / 2)/scale + camera_pos[1]:.2f}"
    coordinates.draw(screen)
    add.draw(screen)
    config_graphs.draw(screen)
    if pygame.mouse.get_pressed()[0]: # left click
        coordinates.check_click(pygame.mouse.get_pos())
        add.check_click(pygame.mouse.get_pos())

def draw_axes():
    pygame.draw.line(screen, LGREY, (0, HEIGHT / 2 - camera_pos[1]*scale), (WIDTH, HEIGHT / 2 - camera_pos[1]*scale), 1) # x-axis
    pygame.draw.line(screen, LGREY, (WIDTH / 2 - camera_pos[0]*scale, 0), (WIDTH / 2 - camera_pos[0]*scale, HEIGHT), 1) # y-axis

if __name__ == "__main__":

    font = pygame.font.SysFont(None, 24)

    coordinates = Button(10, 10, 200, 30, "Example", tp, "abs", 7.5, 7.5)
    add = Button(WIDTH-40, HEIGHT-40, 30, 30, "+", add_graph)
    config_graphs = Button(WIDTH-40, HEIGHT-80, 30, 30, "...", add_graph)

    graphs = []

    for file in os.listdir("generated"):
        if file.endswith(".txt"):
            try:
                graph = Graph(None, f"generated/{file}")
                graph.name = file[:-4]
                graphs.append(graph)
            except Exception as e:
                print(f"Error loading graph from {file}: {e}")

    while True:
        t = clock.tick(60)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                with open("unnamednum.txt", "r") as f:
                    unnamed = int(f.read())
                for i in graphs:
                    if i.name is None:
                        i.name = f"unnamed-{unnamed}"
                        unnamed += 1
                    i.save(f"generated/{i.name if i.name is not None else 'graph'}.txt")
                with open("unnamednum.txt", "w") as f:
                    f.write(str(unnamed))
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    show_ui = not show_ui
        movement(t)
        mouse_movement()
        draw_axes()
        draw_graphs()
        if show_ui:
            text = font.render(f"FPS: {round(clock.get_fps(), 2)}", True, BLACK)
            text_rect = text.get_rect(topright=(WIDTH-10, 10))
            buttons()
            screen.blit(text, text_rect)
        pygame.display.flip()
