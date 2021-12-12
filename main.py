from turtle import Turtle, Screen
import random
import time


screen = Screen()
screen.setup(width = 500, height=400)
screen.bgpic('1beach.png')



def game():
    
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \n You may choose from: red,\norange, yellow, green, blue, purple\nEnter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    
    pen = Turtle()
    pen.hideturtle()

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)
        
    
    is_race_on = True
    if user_bet:
        is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    for turtle in all_turtles:
                        turtle.hideturtle()
                    pen.color(winning_color)
                    if winning_color == user_bet:
                        pen.write(f"You've won!!! The {winning_color} is the winner!!!", align = "center", font=("Calibri", 14, "bold"))
                    else:
                        pen.write(f"You've lost :(. The {winning_color} is the winner!!!", align = "center", font=("Calibri", 14, "bold"))
                    time.sleep(4)
                    again = screen.textinput(title="Play again?", prompt="Would you like to play again? Type 'y' or 'n': ")          
                    pen.clear()          
                    if again == 'y':
                        game()
                    else:
                        screen.bye()
                    
                else:    
                    rand_distance = random.randint(0, 10)
                    turtle.forward(rand_distance)


game()



screen.exitonclick()