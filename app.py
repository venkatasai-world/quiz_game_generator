from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'blue', 'yellow', 'green', 'orange']
positions = [50, -50, 100, -100, 0]
turtles = []
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=positions[i])
    turtles.append(t)
race_on = True

def move_turtles():
    global race_on
    if not race_on:
        return
    for t in turtles:
        t.forward(random.randint(5, 15))
        if t.xcor() >= 230:
            race_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner!")
            return

    screen.ontimer(move_turtles, 100)
move_turtles()
screen.mainloop()
