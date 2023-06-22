import pandas as pd
import turtle

# create screen game
screen = turtle.Screen()
screen.title("U.S. States Game")

# add the map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get the states and location with csv file
data = pd.read_csv('50_states.csv')
all_states = data['state'].to_list()

# create a list to keep the all the answer
guessed_states = []

# start game in loop
while len(guessed_states) < 50:
    # create window for user interface
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # exit the game 
    if answer_state == "Exit":
        break
    
    # check if the answer is in the csv file  
    elif answer_state in all_states:
        # append the guess to the guessed list
        guessed_states.append(answer_state)
        # mark the state in the map after the answer
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# save the names of states the have not being guessed
missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pd.DataFrame(missing_states)
new_data.to_csv('states_to_learning.csv')
