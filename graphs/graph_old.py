import turtle, math, time

class formula:
    def __init__(self, formula):
        self.fstr = formula

    def gen(self, min=-5, max=5, steps=1, max_step=100, log=False, logcmd=print):
        self.path = []
        for i in range(min*max_step, max*max_step, int((-1*max_step)*(min-max)/steps)):
            success, out = self.calc(i/max_step)
            if success:
                self.path.append([i/max_step, out])
                if log:
                    logcmd(f"{i/max_step}: {out}")
            else:
                logcmd(f"Could not get value for x: {i}")
        success, out = self.calc(max)
        if success:
            self.path.append([max, out])
        return self

    def calc(self, num):
        f = self.fstr.replace("x", f"({num})")
        try:
            out = eval(f)
            return True, out
        except:
            return False, 0
        
    def save(self, name):
        txt = ""
        for i in self.path:
            txt += ", ".join([str(i[0]), str(i[1])]) + "\n"
        with open(name, "w") as f:
            f.write(txt)

    def load(self, name):
        self.path = []
        with open(name, "r") as f:
            txt = f.readlines()
        for i in txt:
            pos = i.split(", ")
            self.path.append([float(pos[0]), float(pos[1])])
        return self
        
class graph:
    turtles = {}
    grid = turtle.Turtle()
    grid.speed(0)
    grid.up()
    grid.hideturtle()
    def __init__(self, size=50):
        self.size = size
        self.screen = turtle.Screen()

    def load(self, table: formula, color="grey", width=1, poi=False, label=True):
        if len(table.path) == 0:
            print("No Path Data. Path data not generated or invalid formula.")
            return
        t = turtle.Turtle()
        t.up()
        t.width(width)
        size = self.size
        t.color(color)
        self.turtles[table.fstr] = [t, table]
        t.speed(0)
        t.goto(table.path[0][0]*size, table.path[0][0]*size)
        t.down()
        
        for i in table.path:
            t.goto(i[0]*size, i[1]*size)
            if poi:
                t.dot()
        t.hideturtle()
        if label:
            t.write(table.fstr)
        return t

    def mainloop(self, exitonclick=False):
        if exitonclick:
            self.screen.exitonclick()
        elif exitonclick == False:
            self.screen.mainloop()

    def drawgrid(self, x, y, color=("#e3e3e3", "black")):
        grid = self.grid
        grid.setheading(0)
        grid.clear()
        grid.showturtle()
        size = self.size
        grid.color(color[0])
        for i in range(x[0], x[1], 1):
            grid.goto(y[0]*size, i*size)
            grid.down()
            grid.forward(-1*(y[0]-y[1])*size)
            grid.up()
        grid.setheading(90)
        for i in range(y[0], y[1], 1):
            grid.goto(i*size, x[0]*size)
            grid.down()
            grid.forward(-1*(x[0]-x[1])*size)
            grid.up()
        grid.goto(x[0]*size, 0)
        grid.setheading(0)
        grid.color(color[1])
        grid.down()
        for i in range(x[0], x[1], 1):
            grid.write(i)
            grid.forward(size)
        grid.up()
        grid.goto(0, y[0]*size)
        grid.setheading(90)
        grid.color("black")
        grid.down()
        for i in range(y[0], y[1], 1):
            grid.write(i)
            grid.forward(size)
        grid.up()
        grid.hideturtle()

    def remove(self, fstr):
        if fstr in self.turtles:
            t = self.turtles[fstr][0].clear()
            del self.turtles[fstr]

    def package_all(self, fname):
        lines = []
        for i in self.turtles:
            lines.append("-next")
            lines.append(i[1].fstr)
            for i in i[1].path:
                lines.append(f"{i[0]}, {i[1]}")
            lines.append("-end")
        with open(fname, "w") as f:
            f.write("\n".join(lines))

    def load_all(self, fname):
        with open(fname, "r") as f:
            lines = f.readlines()
        
testgraph = graph(50)
testgraph.drawgrid((-10, 10), (-10, 10))
f = formula("x**3")
testgraph.load(f.gen(-10, 10, 200), width=2)
testgraph.mainloop()