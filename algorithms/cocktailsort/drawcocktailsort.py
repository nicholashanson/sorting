import drawing
import settings
from globals import squares, values, bars

def swap_bars(bars_canvas, lhs_index, rhs_index):
    drawing.swap_elements( bars_canvas,
                           bars,
                           lhs_index,
                           rhs_index,
                           settings.bar_span )

def swap_squares(squares_canvas, lhs_index, rhs_index):
    drawing.swap_elements( squares_canvas,
                           squares,
                           lhs_index,
                           rhs_index,
                           settings.square_span,
                           dimensions = 2 )
    drawing.swap_elements( squares_canvas,
                           values,
                           lhs_index,
                           rhs_index,
                           settings.square_span,
                           dimensions = 2 )
    
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

def draw_squares_bubble(squares_canvas, index, next_index):
    select_square( squares_canvas, index )
    select_square( squares_canvas, next_index )
    if next_index > index:
        deselect_square( squares_canvas, index - 1 )
    elif index != len( squares) - 1:
        deselect_square( squares_canvas, index + 1 )
    squares_canvas.update_idletasks()

def draw_bars_bubble(bars_canvas, index, next_index):
    bars_canvas.itemconfig( bars[ index ],
                            fill = settings.selected_bar_color )
    bars_canvas.itemconfig( bars[ next_index ],
                            fill = settings.selected_bar_color )
    if next_index > index:
        bars_canvas.itemconfig( bars[ index - 1 ],
                                fill = settings.unsorted_partition_color )
    elif index != len( bars ) - 1:
        bars_canvas.itemconfig( bars[ index + 1 ],
                                fill = settings.unsorted_partition_color )
    bars_canvas.update_idletasks()

def remove_squares_bubble(squares_canvas):
    deselect_square( squares_canvas, 0 )
    deselect_square( squares_canvas, 1 )

def remove_bars_bubble(bars_canvas):
    bars_canvas.itemconfig( bars[ 0 ], 
                            fill = settings.unsorted_partition_color )
    bars_canvas.itemconfig( bars[ 1 ], 
                            fill = settings.unsorted_partition_color ) 

def reset():
    squares.clear()
    values.clear()
    bars.clear()




    