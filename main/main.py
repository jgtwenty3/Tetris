from settings import *
from sys import exit

import sqlite3
# components
from game import Game
from score import Score
from preview import Preview

from random import choice


class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Definitely not exactly Tetris')

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        # components
        self.score = Score()
        self.preview = Preview()

        # db
        self.conn = sqlite3.connect('playerscores.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT,
                score INTEGER,
                message TEXT
            )
        ''')

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    

    def run(self):
        game = Game(self.get_next_shape, self.update_score,self.cursor)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            # updating game
            pygame.display.update()
            self.clock.tick()


if __name__ == '__main__':
    main = Main()
    main.run()