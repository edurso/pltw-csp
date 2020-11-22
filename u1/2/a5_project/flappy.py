#!/usr/bin/env python3

import random as rand
import turtle as trtl

# class for gravity object
class Grav():
    # constructor initilizes values
    def __init__(self, grav, grav_inc, inverse) -> None:
        self.grav = grav
        self.grav_inc = grav_inc
        self.inverse = inverse
    # returns value of gravity multiplier
    def get_grav(self) -> int:
        return self.grav
    # sets gravity multiplier
    def set_grav(self, grav) -> None:
        self.grav = grav
    # increments gravity coefficient
    def increment(self) -> None:
        self.grav += self.grav_inc
    # invert gravity value to make bird go up
    def invert(self) -> None:
        self.grav = self.inverse

# class for a set of pipes
class Pipe():
    # constructor creates new pipe object and sets its position
    def __init__(self, x, stroke, filepath, pipe_range_low, pipe_range_high, pipe_spacing, top_pipe_path, bottom_pipe_path) -> None:
        self.stroke = stroke
        self.x = x
        self.filepath = filepath 
        height_top = rand.randint(pipe_range_low, pipe_range_high)
        height_bottom = height_top - pipe_spacing 
        self.top = trtl.Turtle(shape=(self.filepath + top_pipe_path))
        self.top.hideturtle()
        self.top.speed('fastest')
        self.top.penup()
        self.top.setx(x)
        self.top.sety(height_top)
        self.top.showturtle()
        self.bottom = trtl.Turtle(shape=(self.filepath + bottom_pipe_path))
        self.bottom.hideturtle()
        self.bottom.speed('fastest')
        self.bottom.penup()
        self.bottom.setx(x)
        self.bottom.sety(height_bottom)
        self.bottom.showturtle()
    # function moves the pipe by the configured step
    def move(self) -> None:
        self.x -= self.stroke
        self.top.setx(self.top.xcor()-self.stroke)
        self.bottom.setx(self.bottom.xcor()-self.stroke)
    # function returns the x position of the pipe set
    def getx(self) -> int:
        return self.x
    # function returns the y position of the top pipe
    def get_topy(self) -> int:
        return self.top.ycor()
    # function returns the y position of the bottom pipe
    def get_bottomy(self) -> int:
        return self.bottom.ycor()
    # function removes the pipes from view 
    def hide(self) -> None:
        self.top.clear()
        self.top.hideturtle()
        self.bottom.clear()
        self.bottom.hideturtle()

# class for a user's score
class Score():
    # constructor initilizes score of 0
    def __init__(self) -> None:
        self.score = 0
    # function sets score to particular value
    def set(self, score) -> None:
        self.score = score
    # function retrieves score
    def get(self) -> int:
        return self.score

# class for the list of pipes
class PipeSet():
    # constructor creates new, empty list
    def __init__(self) -> None:
        self.pipe_list = []
    # function returns the list of pipes
    def pipes(self) -> list:
        return self.pipe_list
    # functions appends a pipe onto the list
    def append(self, pipe) -> None:
        self.pipe_list.append(pipe)
    # function empties the list of pipes
    def clear(self) -> None:
        self.pipe_list.clear()

# configure constants
GROUND            = -200
LEFT_BORDER       = -600
SCREEN_BOTTOM     = -350
PIPE_STROKE       = 8
PIPE_INIT         = 150
PIPE_SPACING      = 250
SCREEN_WIDTH      = 474
SCREEN_HEIGHT     = 600
PIPE_LOW          = 150
PIPE_HIGH         = 350
PIPE_SPACING_VERT = 500
PIPE_WIDTH        = 60 
PIPE_HEIGHT       = 163
GRAV_COEF         = Grav(grav=8,grav_inc=1,inverse=-12)
FILEPATH          = "./img/"
BIRD_IMG          = "bird.gif"
TOP_PIPE_PATH     = "top-pipe.gif"
BOTTOM_PIPE_PATH  = "bottom-pipe.gif"
BG_IMAGE          = "flappy-bird.gif"
LB_FILE           = "flappy-leaderboard.txt"
KEYS = {
    "SPACE":"space",
    "UP":"Up",
    "Q":"q",
}

pipes = PipeSet()

# function creates a new pipe object
def new_pipe(pos) -> Pipe:
    return Pipe(pos, PIPE_STROKE, FILEPATH, PIPE_LOW, PIPE_HIGH, PIPE_SPACING_VERT, TOP_PIPE_PATH, BOTTOM_PIPE_PATH)

# function to update pipe positions
def update_pipes() -> None:
    for pp in pipes.pipes():
        pp.move()
        if pp.getx() < LEFT_BORDER:
            pp.hide()
            pipes.pipes().remove(pp)
            pipes.pipes().append(new_pipe(pipes.pipes()[len(pipes.pipes())-1].getx() + PIPE_SPACING))

# function to update position of bird
def update_bird(bird) -> None:
    bird.sety(bird.ycor()-1*GRAV_COEF.get_grav())
    GRAV_COEF.increment()

# function to handle key press events
def handle_key() -> None:
    GRAV_COEF.invert()

# function to determine if bird has hit a pipe
def bird_crashed(bird) -> bool:
    ground = bird.ycor() < GROUND
    pipe = False
    for pp in pipes.pipes():
        x = bird.xcor() >= (pp.getx() - PIPE_WIDTH) and bird.xcor() <= (pp.getx() + PIPE_WIDTH)
        topy = bird.ycor() >= (pp.get_topy() - PIPE_HEIGHT) 
        bottomy = bird.ycor() <= (pp.get_bottomy() + PIPE_HEIGHT) 
        pipe = (x and topy) or (x and bottomy)
        if pipe:
            return True
    return ground or pipe

# function makes bird drop from sky
def bird_die(bird) -> None:
    # TODO: Print "Game Over"
    while bird.ycor() > SCREEN_BOTTOM:
        bird.sety(bird.ycor()-1)

def update_score() -> None:
    # TODO: Implement
    return None

# function initilizes the game screen
# must be called before `play_game` method
def init() -> trtl.Turtle:
    wn = trtl.Screen()
    pipes.clear()
    wn.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    wn.bgpic(FILEPATH + BG_IMAGE)
    wn.register_shape(FILEPATH + BIRD_IMG)
    wn.register_shape(FILEPATH + TOP_PIPE_PATH)
    wn.register_shape(FILEPATH + BOTTOM_PIPE_PATH)
    for i in range(5):
        pipes.append(new_pipe(PIPE_INIT + i*PIPE_SPACING))
    bird = trtl.Turtle(shape=(FILEPATH+BIRD_IMG))
    bird.penup()
    return bird

# game function
def play_game(bird) -> int:
    score = 0
    # TODO: Print Countdown In Score
    while not bird_crashed(bird):
        update_bird(bird)
        update_pipes()
        update_score()
    bird_die(bird)
    return score
