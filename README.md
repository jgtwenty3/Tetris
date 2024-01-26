This is a python application that emulates a Tetris game. It is connected to a db using SQL. 

The game is made of: 

main.py: 
  -initializes pygame, sets general display, connects to db, 
settings.py: 
  -game settings (ex: game size, colors, tetromino shapes,etc.)
game.py: 
  - main game functions
  - draw grid, create tetrominos, caclculate score, key inputs, collision, game over logic, etc.
timer.py:
  - establishes timers for the game
preview.py:
  - display and logic for preview of next tetrominos
score.py:
  - display for score
playerscore.db:
  - Player id, name, socre, and message

to do still: 
  - create the display in game for game over. user should be able to input on game display instead of in terminal
  - create starting menu to either initialize game or check list of high scores
  - add sound
