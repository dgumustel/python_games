# Minesweeper in Python

This game is currently functional, but not pretty! After a bit of looking around, it may be worth it to swap from using tkinter to using pygame. 

Bugs: 
- Still able to right-click and flag opened cells that are touching mines or touching the edge of the board

Below is a list of additional features, in no particular order, that I'd like to incorporate:
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
- Ensure that games are solvable without guessing (this will be a challenge because it requires programming a board solver, see resources) 
- Reveal mines on game over (win or lose) including places where player incorrectly flagged mines
- Troubleshoot tkinter display failures on MacOS - might become an obsolete issue if I swap to using pygame
- When clicking on a cell whose number is equal to the number of neighboring flags, reveal surrounding unflagged cells
- Add buttons to restart board, start new game, or change settings

Resources:
- Free code camp tutorial: [https://www.youtube.com/watch?v=OqbGRZx4xUc](https://www.youtube.com/watch?v=OqbGRZx4xUc)
- Inspiration: [https://github.com/franciscod/puzzles/blob/master/mines.c](https://github.com/franciscod/puzzles/blob/master/mines.c)
- Minesweeper in Pygame 1: [https://github.com/vdallco/Minesweeper](https://github.com/vdallco/Minesweeper)
- Minesweeper in Pygame 2 (runs smoother than the first): [https://github.com/Harrelix/Minesweeper](https://github.com/Harrelix/Minesweeper)

Note that this subdirectory was merged from another repository into the python_games repo following these instructions: https://gist.github.com/msrose/2feacb303035d11d2d05 
