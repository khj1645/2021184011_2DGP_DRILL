from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global dirX
    global dirY
    global anim
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                anim = 1
                dirX += 1
            elif event.key == SDLK_LEFT:
                anim = 0
                dirX -= 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                anim = 3
                dirX -= 1
            elif event.key == SDLK_LEFT:
                anim = 2
                dirX += 1
            elif event.key == SDLK_DOWN:
                dirY += 1
            elif event.key == SDLK_UP:
                dirY -= 1


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
anim = 3

while running: 
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, anim * 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if (x < TUK_WIDTH - 20 and dirX == 1) or (x > 20 and dirX == -1):
        x += dirX * 5
    if (y < TUK_HEIGHT - 35 and dirY == 1) or (y > 35 and dirY == -1):
        y += dirY * 5
    delay(0.01)

close_canvas()
