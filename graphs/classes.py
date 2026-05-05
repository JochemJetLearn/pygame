import pygame, math, random
from constants import *

class float_range:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current

class Button:
    
    def __init__(self, x, y, width, height, text, onclick, display_mode="rel", xmargin=None, ymargin=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.onclick = onclick
        self.display_mode = display_mode
        if display_mode == "abs" and (xmargin is not None and ymargin is not None):
            self.xmargin = xmargin
            self.ymargin = ymargin
        else:
            self.display_mode = "rel"
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, screen):
        col = GREY if self.rect.collidepoint(pygame.mouse.get_pos()) else LGREY
        pygame.draw.rect(screen, col, self.rect)
        
        text = self.font.render(self.text, True, BLACK)
        if self.display_mode == "rel":
            text_rect = text.get_rect(center=self.rect.center)
        elif self.display_mode == "abs":
            text_rect = text.get_rect(topleft=(self.rect.x+self.xmargin, self.rect.y+self.ymargin))
        screen.blit(text, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.onclick()

class Graph:
    def __init__(self, func, file=None):
        if callable(func):
            self.func = func
        self.points = {}
        self.func_str = None
        if type(file) == str:
            with open(file, "r") as f:
                lines = f.readlines()
                self.func_str = lines[0].strip()
                self.func = eval(f"lambda x, z: {self.func_str}")
                for line in lines[1:]:
                    x, y = line.strip().split(",")
                    self.points[float(x)] = float(y)
        self.color = BLACK
        self.name = "Graph"
    
    def save(self, save_name):
        with open(save_name, "w") as f:
            f.write(f"{self.func_str if self.func_str is not None else "0"}\n")
            for x, y in self.points.items():
                f.write(f"{x}, {y}\n")

    def calculate_points(self, x_range, save=False, save_name=None):
        z = x_range.start - x_range.step
        for i in x_range:
            x = round(i, 10)
            if x in self.points:
                continue
            y = self.func(x, z)
            self.points[x] = y
            z = x
        if save and save_name is not None:
            self.save(save_name)
    
    def draw(self, screen, camera_pos, scale, x_range, size=1, points=False):
        try:
            mouse_pos = pygame.mouse.get_pos()
            last_x = None
            last_y = None
            for i in x_range:
                x = round(i, 10)
                y = self.points[x]
                screen_x = int((x - camera_pos[0]) * scale + WIDTH / 2)
                screen_y = int((y - camera_pos[1]) * scale + HEIGHT / 2)
                if points:
                    pygame.draw.circle(screen, self.color, (screen_x, screen_y), 2)
                if last_x is not None:
                    #if abs(y - last_y*scale) < HEIGHT*2: # only draw if the line is not too long (to avoid drawing lines across the screen when there are gaps in the function)
                        pygame.draw.line(screen, self.color, (last_x//1, last_y//1), (screen_x//1, screen_y//1), size)
                        if point_line_collision(mouse_pos[0], mouse_pos[1], last_x//1, last_y//1, screen_x//1, screen_y//1, threshold=15):
                            font = pygame.font.SysFont(None, 24)
                            nametext = font.render(f"{self.name if self.name != None else "Graph"}", True, BLACK, LGREY)
                            functext = font.render(f"f(x) = {self.func_str}" if self.func_str is not None else f"f(x) = {self.func.__name__}(x)", True, BLACK, LGREY)
                            name_rect = nametext.get_rect(bottomleft=(mouse_pos[0]+10, mouse_pos[1]+10))
                            funct_rect = functext.get_rect(topleft=(name_rect.x, name_rect.y + name_rect.height))
                            screen.blit(nametext, name_rect)
                            screen.blit(functext, funct_rect)
                last_x = screen_x
                last_y = screen_y
        except KeyError:
            self.calculate_points(x_range)
            self.draw(screen, camera_pos, scale, x_range)
        except Exception as e:
            return

def point_line_collision(px, py, ax, ay, bx, by, threshold=0.001):
    
        min_x, min_y = ax, ay
        max_x, max_y = bx, by
        if bx < ax:
            min_x = bx
            max_x = ax
        if by < ay:
            min_y = by
            max_y = ay
    
        if not ( px >= min_x and px < min_x + (max_x-min_x) ) and ( py >= min_y and py < min_y + (max_y-min_y) ): # bounding box rect collision check to return early 
            return False
    
        vec1_x = px-ax   #vec1: Position vector of the point (px, py)  
        vec1_y = py-ay  
        vec2_x = bx-ax    #vec2: vector describing the line segment (ax, ay) to (bx, by)
        vec2_y = by-ay

        vec2_scalar = (vec2_x*vec2_x + vec2_y*vec2_y)
        if vec2_scalar == 0: # if the line segment is actually a point
            return ((px-ax)**2 + (py-ay)**2)**0.5 <= threshold
        
        vec3_scalar = (vec1_x*vec2_x + vec1_y*vec2_y) / (vec2_x*vec2_x + vec2_y*vec2_y)    # based on https://en.wikipedia.org/wiki/Vector_projection
        vec3_x = vec3_scalar*vec2_x   #vec3: The projection of vector vec1 unto vec2  
        vec3_y = vec3_scalar*vec2_y
        dist_a = ((vec1_x-vec3_x)**2 + (vec1_y-vec3_y)**2)**0.5    # distance of the mouse position to the line segment
        # (distance to the infinite line that it is parallel to) or distance between the vectors vec1 and vec3
    
        dist_b = ((vec2_x-vec3_x)**2 + (vec2_y-vec3_y)**2)**0.5  # distance between the vectors vec2 and vec3
        dist_c = (vec2_x*vec2_x + vec2_y*vec2_y)**0.5  # length of vec3 (line segment length)
        condition1 = ( abs(vec3_x) <= abs(vec2_x) ) and ( abs(vec3_y) <= abs(vec2_y) )  # checks if the absolute coordinates of vec3 are smaller than those of vec2
        
        return (dist_b <= dist_c) and condition1 and dist_a <= threshold

