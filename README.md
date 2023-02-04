# Minesweeper in Python

This game is currently functional, but not pretty! Below is a list of ideas, in no particular order, that I'd like to incorporate:

- Settings for different game difficulties currently exist in settings.py but are not utilized
- The GUI is not satisfactory 
- There's no way to actually flag mines, and no count of flagged mines 
- Clicking on 0s correctly opens neighboring cells, but not the neighboring cells of newly uncovered 0s
- Game over (win or lose) needs to offer a "play again" option 
- The GUI needs work
- Consider adding stats like game time
- Consider making it playable in a web browser
- Add an image for mines
- Color-code the numbers in opened cells
- Have I mentioned that the GUI is bad? Please fix the GUI
- Add the little smiley face that goes :O when you click on a cell
- Ensure that every starting click is a safe click (requires board generation on first click rather than on start-up) 
- Ensure that games are solvable without guessing (this will be a challenge, see resources) 
- Reveal mines on game over (win or lose) including places where player incorrectly flagged mines

Resources:
- Free code camp tutorial: [https://www.youtube.com/watch?v=OqbGRZx4xUc](https://www.youtube.com/watch?v=OqbGRZx4xUc)
- Inspiration: [https://github.com/franciscod/puzzles/blob/master/mines.c](https://github.com/franciscod/puzzles/blob/master/mines.c)
