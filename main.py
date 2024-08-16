import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
total_guesses = []

while len(total_guesses) < 50:
    user_input = screen.textinput(title=f"{len(total_guesses)}/50 Guess the state",
                                  prompt="What's the state name?").title()

    if user_input == "Exit":
        # using comprehension
        missed_states = [state for state in all_states if state not in total_guesses ]

        # use regular for loop
        # for state in all_states:
        #     if state not in total_guesses:
        #         missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_input in all_states:
        total_guesses.append(user_input)
        new_t = turtle.Turtle()
        new_t.hideturtle()
        new_t.penup()
        state_data = data[data.state == user_input]
        new_t.goto(state_data.x.item(), state_data.y.item())
        new_t.write(user_input)
