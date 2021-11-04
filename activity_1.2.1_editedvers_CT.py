# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
shape = "triangle"
shapes = ["classic", "circle", "square", "triangle"]
size = 4
sizes = [0.5, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8]
score = 0
timer = 30
counter_interval = 1000
timer_up = False
font_setup = ("Arial", 20, "normal")
font_setup2 = ("Arial", 50, "normal")
color = "black"
colors = ["dodgerblue", "deepskyblue", "gold", "mediumorchid", "lightpink", "darkturquoise", "black"]
angle = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350]


#-----initialize turtle-----
johnathan = t.Turtle()
johnathan.speed(0)
score_writer = t.Turtle()
game_starter_thing = t.Turtle()
game_starter_thing.hideturtle
game_starter_thing.penup()
counter = t.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-400, 280)
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(300, 280)

#-----game functions--------
johnathan.shape(shape)
johnathan.shapesize(size)
johnathan.fillcolor(color)
johnathan.hideturtle()
def add_color():
    johnathan.fillcolor(rand.choice(colors))
    johnathan.stamp()
    johnathan.fillcolor(color)
def add_shape():
    johnathan.shape(rand.choice(shapes))
def change_angle():
    johnathan.right(rand.choice(angle))
def change_size():
    johnathan.shapesize(rand.choice(sizes))
def johnathan_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        johnathan.hideturtle()
def change_position():
  new_xpos = rand.randint(-400, 400)
  new_ypos = rand.randint(-300, 300)
  johnathan.penup()
  johnathan.hideturtle()
  johnathan.goto(new_xpos, new_ypos)
  johnathan.showturtle()
  johnathan.pendown()
  change_size()
  change_angle()
  add_shape()
  add_color()
  johnathan.shapesize(size)
  johnathan.shape(shape)
def update_score():
  score_writer.clear()
  global score 
  score = score + 1
  score_writer.write(score, font=font_setup)
  

#-----events----------------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
wn = t.Screen()
wn.bgcolor("darkorange")
game_starter_thing.goto(-350,0)
game_starter_thing.write("Press here to start", font=font_setup2)
game_starter_thing.goto(300, 0)
game_starter_thing.showturtle()
game_starter_thing.color("red")
game_starter_thing.shape("circle")
def timer_and_click_functions():
    wn.ontimer(countdown, counter_interval)
    johnathan.showturtle()
    johnathan.onclick(johnathan_clicked)
def game_start(x,y):
    game_starter_thing.onclick(timer_and_click_functions)
    game_starter_thing.clear()
    game_starter_thing.hideturtle()
    timer_and_click_functions()
game_starter_thing.onclick(game_start)
wn.mainloop()