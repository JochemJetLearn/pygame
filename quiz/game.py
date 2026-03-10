import pgzrun

WIDTH = 800
HEIGHT = 700

questions_file = "python_game_dev/quiz/questions.txt"
questions = []
question = []
options = []

moving_box = Rect(0, 0, 800, 100)

answerbox1 = Rect(100, 300, 200, 100)
answerbox2 = Rect(350, 300, 200, 100)
answerbox3 = Rect(100, 450, 200, 100)
answerbox4 = Rect(350, 450, 200, 100)
answerboxes = [answerbox1, answerbox2, answerbox3, answerbox4]

questionbox = Rect(100, 150, 600, 100)
skipbox = Rect(600, 450, 100, 100)
scorebox = Rect(600, 300, 100, 100)

score = 0

def update():
    moving_box.x -= 5
    if moving_box.x < -800:
        moving_box.x = 800

def read_next_question():
    if len(questions) > 0:
        return questions.pop(0)
    else:
        return ["Quiz over", "", "", "", "", "0"]

def read_questions():
    with open(questions_file, "r") as file:
        for line in file:
            questions.append(line.strip().split(","))

def draw():
    screen.fill("white")
    screen.draw.filled_rect(moving_box, "green")
    screen.draw.textbox("Welcome to the quiz!", moving_box, color="black")
    screen.draw.filled_rect(answerbox1, "orange")
    screen.draw.filled_rect(answerbox2, "orange")
    screen.draw.filled_rect(answerbox3, "orange")
    screen.draw.filled_rect(answerbox4, "orange")
    screen.draw.filled_rect(questionbox, "orange")
    screen.draw.textbox(question[0], questionbox, color="black")
    screen.draw.filled_rect(skipbox, "red")
    screen.draw.textbox("Skip", skipbox, color="white")
    screen.draw.filled_rect(scorebox, "blue")
    screen.draw.textbox(f"Score:\n{score}", scorebox, color="white")
    index = 1
    for i in answerboxes:
        screen.draw.textbox(question[index], i, color="black")
        index += 1

def on_mouse_down(pos):
    global answerboxes, score, question
    answer = int(question[5])
    for i in range(4):
        if answerboxes[i].collidepoint(pos):
            if i+1 == answer:
                score += 1
            question = read_next_question()
    if skipbox.collidepoint(pos):
        question = read_next_question()

read_questions()
question = read_next_question()
pgzrun.go()
