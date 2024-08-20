import turtle

import pandas
guessed_states=[]

screen=turtle.Screen()
score=0
screen.title("India State Game")
image="political.gif"
screen.setup(800,800)
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("Indian_states.csv")
all_list=data.state.to_list()
while len(guessed_states)<50:
    answer_input = screen.textinput(title=f"{score}/27 states correct", prompt="write the name of a state?").title()

    if answer_input in all_list:
        score=score+1
        guessed_states.append(answer_input)
        new_turtle=turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()

        row=data[data.state == answer_input]
        new_turtle.goto(row.x.item(),row.y.item())
        new_turtle.write(answer_input)

    if answer_input=="Exit":
        missing_states = []
        for item in all_list:
            if item not in guessed_states:
                missing_states.append(item)
        need_to_learn=pandas.DataFrame(missing_states)
        need_to_learn.to_csv("states to learn")
        break


screen.exitonclick()