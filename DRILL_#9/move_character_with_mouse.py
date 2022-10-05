from pico2d import *
import random

def move():
    global x,y,frame,p1,p2
    for i in range(0, 100 + 1, 1):
        clear_canvas()
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(hand_x,hand_y)
        character.clip_draw(frame * 100, 100 * anim, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x = random.randint(0,TUK_WIDTH)
hand_y = random.randint(0,TUK_HEIGHT)
p1 = [x,y]
p2 = [hand_x,hand_y]
frame = 0
hide_cursor()

while running:
    if(p2[0] > p1[0]):
        anim = 1
    else:
        anim = 0
    move()
    hand_x = random.randint(0,TUK_WIDTH)
    hand_y = random.randint(0,TUK_HEIGHT)
    p1 = [x,y]
    p2 = [hand_x,hand_y]

close_canvas()




