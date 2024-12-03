import drawing
import settings
from globals import squares, values, bars

def swap_bars(bars_canvas, index):
    drawing.swap_elements( bars_canvas,
                           bars,
                           index,
                           index + 1,
                           settings.bar_span )

def swap_squares(squares_canvas, index):
    drawing.swap_elements( squares_canvas,
                           squares,
                           index,
                           index + 1,
                           settings.square_span,
                           dimensions = 2 )
    drawing.swap_elements( squares_canvas,
                           values,
                           index,
                           index + 1,
                           settings.square_span,
                           dimensions = 2 )

def select_bar(bars_canvas, index):
    bars_canvas.itemconfig( bars[ index ],
                            fill = settings.selected_bar_color )
    
def deselect_bar(bars_canvas, index):
    bars_canvas.itemconfig( bars[ index ],
                            fill = settings.unsorted_partition_color )
    
def select_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.text_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.unsorted_partition_color )

def deselect_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.unsorted_partition_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.text_color )

def draw_squares_bubble(squares_canvas, index):
    select_square( squares_canvas, index )
    select_square( squares_canvas, index + 1 )  
    
    if index == 0:
        deselect_square( squares_canvas, -1 )
        deselect_square( squares_canvas, -2 )
    else: 
        deselect_square( squares_canvas, index - 1 )
    squares_canvas.update_idletasks()

def draw_bars_bubble(bars_canvas, index):
    select_bar( bars_canvas, index )
    select_bar( bars_canvas, index + 1 )

    if index == 0:
        deselect_bar( bars_canvas, -1 )
        deselect_bar( bars_canvas, -2 )
    else:
        deselect_bar( bars_canvas, index - 1 )
    bars_canvas.update_idletasks()

def remove_squares_bubble(squares_canvas):
    deselect_square( squares_canvas, -1 )
    deselect_square( squares_canvas, -2 )

def remove_bars_bubble(bars_canvas):
    deselect_bar( bars_canvas, -1 )
    deselect_bar( bars_canvas, -2 )

def reset():
    squares.clear()
    values.clear()
    bars.clear()



    