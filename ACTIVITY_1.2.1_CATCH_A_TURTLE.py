# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
shape = "triangle"
size = 10
color = "blue"
score = 0
timer = 30
counter_interval = 1000
timer_up = False
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
johnathan = t.Turtle()
score_writer = t.Turtle()
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
def johnathan_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        johnathan.hideturtle()
def change_position():
  new_xpos = rand.randint(0, 400)
  new_ypos = rand.randint(0, 300)
  johnathan.penup()
  johnathan.hideturtle()
  johnathan.goto(new_xpos, new_ypos)
  johnathan.showturtle()
  johnathan.pendown()
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
johnathan.onclick(johnathan_clicked)
wn = t.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()