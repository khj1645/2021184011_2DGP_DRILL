from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
}


# 상태 정의
class IDLE:
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000
        pass

    def exit(self):  # 상태를 나올 때 행하는 액션
        print('EXIT IDLE')
        pass

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER) # 객체지향적인 방법
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        # 어떤 키가 눌렸는지로 방향을 결정해야함
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass


class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0
        self.timer = 0
        pass

    def exit(self):
        print('EXIT SLEEP')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        if self.timer < 1000:
            self.timer += 10
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

    pass


class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO RUN')
        if self.dir == 0:
            self.dir = self.face_dir
        pass

    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir
        self.dir = 0
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        if self.dir == 1:
            self.x += 1
            self.x = clamp(0, self.x, 800)
            if self.x >= 800:
                self.dir = -1
        elif self.dir == -1:
            self.x -= 1
            self.x = clamp(0, self.x, 800)
            if self.x <= 0:
                self.dir = 1
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y + 25, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y + 25, 200, 200)
        pass

# 상태 변환 기술
next_state = {
    AUTO_RUN: {RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN, LD: RUN, TIMER: AUTO_RUN, AD: IDLE},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, TIMER: RUN, AD: AUTO_RUN},
}


class Boy:

    def add_event(self, event):
        self.q.insert(0,event)

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.q = []  # 이벤트 큐 초기화

        self.cur_state = IDLE
        self.cur_state.enter(self, None)  # 초기 상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self)  # 현재 상태의 do 수행

        # 이벤트 확인해서 이벤트가 있으면 변환

        if self.q:  # 큐에 이벤트가 있으면
            event = self.q.pop()
            self.cur_state.exit(self)  # 현재 상태 나감
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 구한다
            self.cur_state.enter(self, event)  # 다음 상태의 entry 액션 수행행

        # self.frame  (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

