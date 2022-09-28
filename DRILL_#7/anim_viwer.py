from pico2d import *
open_canvas()
character = load_image('sprite.png')

def draw_anim(frame,y):
    for x in range(0,frame,1):
        clear_canvas()
        character.clip_draw(55 * x, y, 55, 63, 400, 300)
        update_canvas()
        delay(0.1)
        
while True:
    for y in range(0,5):
        draw_anim(4,378 - 63 * y)
    for y in range(0,2):
        draw_anim(5,63 - 63 * y)
        
close_canvas()

