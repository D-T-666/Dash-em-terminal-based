from random import randint
import os
import time
import sys

Terminal_Rows, Terminal_Cols = [
    *map(int, os.popen('stty size', 'r').read().split())]


class Board:
    def __init__(self):
        self.tiles = ["  ",
                      "\u001b[38;5;22m▄▀\u001b[0m",
                      "\u001b[38;5;46m██\u001b[0m",
                      "\u001b[38;5;220m██\u001b[0m"]

        self.player = (1, 1)
        self.player_v = (0, 0)

    def _load_map(self):
        self.map = []
        for i in range(8):
            self.map.append([])
            for j in range(8):
                tile: int
                if (i == 0 or i == 7) or (j == 0 or j == 7):
                    tile = 2
                else:
                    tile = randint(0, 3)
                self.map[i].append(tile)
        print(self.map)

    def _update_spot(self):
        p = self.map[self.player[0]][self.player[1]]
        np = 0

        if p == 0 or p == 3:
            np = 1
        if p == 1:
            np = 2

        self.map[self.player[0]][self.player[1]] = np

    def _update(self):
        if self.map[self.player[0]+self.player_v[0]][self.player[1]+self.player_v[1]] in [0, 1, 3]:
            self.player = (self.player[0]+self.player_v[0],
                           self.player[1]+self.player_v[1])
            self._update_spot()
        else:
            return False
        return True

    def _start_moving(self, direction):
        self.player_v = direction
        while self._update():
            os.system("clear")
            print(self)
            time.sleep(0.01)

    def _has_won(self):
        return sum([row.count(3) for row in self.map]) == -8

    def _auto_tile(self, i, j):
        tilemap = [["??" for _ in range(4)] for _ in range(4)]

        if self.map[i % 8][j % 8] == 0:
            for k in range(4):
                for p in range(4):
                    tilemap[p][k] = self.tiles[0]

        if self.map[i % 8][j % 8] == 1:
            for k in range(4):
                for p in range(4):
                    tilemap[p][k] = self.tiles[1]

        if self.map[i % 8][j % 8] == 2:
            for k in range(4):
                for p in range(4):
                    tilemap[p][k] = self.tiles[0]

            if self.map[(i+0) % 8][(j+1) % 8] != 2:
                for k in range(4):
                    tilemap[k][3] = self.tiles[2]

            if self.map[(i+0) % 8][(j-1) % 8] != 2:
                for k in range(4):
                    tilemap[k][0] = self.tiles[2]

            if self.map[(i+1) % 8][(j+0) % 8] != 2:
                for k in range(4):
                    tilemap[3][k] = self.tiles[2]

            if self.map[(i-1) % 8][(j+0) % 8] != 2:
                for k in range(4):
                    tilemap[0][k] = self.tiles[2]

            if self.map[(i+1) % 8][(j+1) % 8] != 2:
                tilemap[3][3] = self.tiles[2]
            if self.map[(i+1) % 8][(j-1) % 8] != 2:
                tilemap[3][0] = self.tiles[2]
            if self.map[(i-1) % 8][(j+1) % 8] != 2:
                tilemap[0][3] = self.tiles[2]
            if self.map[(i-1) % 8][(j-1) % 8] != 2:
                tilemap[0][0] = self.tiles[2]

        if self.map[i][j] == 3:
            for k in range(4):
                for p in range(4):
                    tilemap[p][k] = self.tiles[0]
            for k in range(1, 3):
                for p in range(1, 3):
                    tilemap[p][k] = self.tiles[3]

        tilemap = ["".join(row) for row in tilemap]
        return tilemap

    def __str__(self):
        board = ("\n"*((Terminal_Rows-32)//2))+(" "*((Terminal_Cols-64)//2))
        for i in range(8*4):
            for j in range(8):
                if self.player != (i//4, j):
                    board += self._auto_tile(i//4, j)[i % 4]
                else:
                    board += ["\u001b[38;5;39m████████\u001b[0m",
                              "\u001b[38;5;39m██    ██\u001b[0m",
                              "\u001b[38;5;39m██    ██\u001b[0m",
                              "\u001b[38;5;39m████████\u001b[0m"][i % 4]
            board += "\n" + (" "*((Terminal_Cols-64)//2))
        return board

    def _display(self):
        os.system("clear")

        sys.stdout.write("the board")
        sys.stdout.flush()
