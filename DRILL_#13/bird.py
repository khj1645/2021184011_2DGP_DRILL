from pico2d import *
import random
import time

frame_time = 0.0


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


def handle_event():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

class Bird:
    image = None
    def __init__(self):
        self.dir = 1
        self.frame = 0
        self.x = random.randint(200, 700)
        self.y = random.randint(100, 600)
        if Bird.image == None:
            self.image = load_image('bird_animation.png')
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * frame_time
        if self.x + 90 >= 1000:
            self.dir = -1
        if self.x - 90 <= 0:
            self.dir = 1
        pass
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 180, 336, 180, 168, self.x, self.y, 180, 168)
        else:
            self.image.clip_composite_draw(int(self.frame) * 180, 336, 180, 168,
                                           0.0, 'h', self.x, self.y, 180, 168)
        pass

running = True
open_canvas(1000, 800)
birds = [Bird() for i in range(10)]
current_time = time.time()
while running:
    clear_canvas()
    handle_event()

    for bird in birds:
        bird.update()

    for bird in birds:
        bird.draw()
    frame_time = time.time() - current_time
    frame_rate = 1.0 / frame_time
    current_time += frame_time

    update_canvas()

