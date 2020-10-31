from pynput.keyboard import Key
from .board import Board, os


class GameLoop:
    def __init__(self):
        # Initialize the data
        self.board = Board()

        # Load the map
        self.board._load_map()

        # print the board
        os.system("clear")
        print(self.board)

    def _start_loop(self):
        # while True:
        self._loop()

    def _loop(self):
        # while (cmd := input()):
        print("Started the loop!")

    def _key_press_event(self, a):
        try:
            if a.char == 'w':
                self.board._start_moving((-1, 0))
            if a.char == 'a':
                self.board._start_moving((0, -1))
            if a.char == 's':
                self.board._start_moving((1, 0))
            if a.char == 'd':
                self.board._start_moving((0, 1))
            if a.char == 'q':
                exit()
            if self.board._has_won():
                print("you win!")
                exit()
        except AttributeError:
            pass
        # self.board._display()
        os.system("clear")
        print(self.board)

    def _key_release_event(self, a):
        # print('released', a)
        pass
