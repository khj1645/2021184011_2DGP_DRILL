import pico2d
import logo_state
import play_state

start_state = logo_state  # 모듈을 변수로 취급

pico2d.open_canvas()
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        state.delay(0.05)
    state.exit()
start_state.enter()
pico2d.close_canvas()