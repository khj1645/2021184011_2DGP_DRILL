from pico2d import *
import math
global W
global L
W = 42
L = 92
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_square(x,y):
    
    while x < 800 - W:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)

    while y < 600 - L:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)

    while x > 10:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)

    while x < 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)
        
def move_circle(x,y):
    for angle in range(270,630):
        clear_canvas_now()
        x =  400 + (math.cos(angle * (3.14 / 180)) * 210)
        y =  300 + (math.sin(angle * (3.14 / 180)) * 210)
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

while True:
    x = 400
    y = 90
    move_circle(x,y)
    move_square(x,y)
    
    
close_canvas()

