from tkinter import *
from cell import Cell
import settings # custom settings file
import utils

root = Tk() # create window class

# Change settings of root window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False) # stop people from resizing window (width, height)

# Create a frame for top of window
top_frame = Frame(
    root, 
    bg='gray', # TODO: change to black
    width=settings.WIDTH, # span full width
    height=utils.height_prct(25)
) # Frame class 
# Place this top sidebar using top left corner as anchor 
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper',
    font=('', 48)
)
game_title.place(
    x=utils.width_prct(25),
    y=0
)

left_frame = Frame(
    root,
    bg='dark gray', # TODO: change
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black', # TODO: change
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25))

for x in range(settings.GRID_WIDTH): 
    for y in range(settings.GRID_HEIGHT):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call label from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

for c in Cell.all:
    print(c.is_mine)

# Run window
root.mainloop()


