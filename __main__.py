from src import GameLoop
from pynput.keyboard import Listener

my_game = GameLoop()

with Listener(
        on_press=my_game._key_press_event,
        on_release=my_game._key_release_event) as listener:
    listener.join()

my_game._start_loop()