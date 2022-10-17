import pico2d
import game_framework

import play_state
import item_state
import logo_state

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.clear_canvas()

