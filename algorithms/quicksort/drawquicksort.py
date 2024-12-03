import settings
import drawing
from globals import squares, values, bars

previous_indexes = [None, None]

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
    
def swap_bars(bars_canvas, lhs_index, rhs_index):
    drawing.swap_elements( bars_canvas, 
                           bars, 
                           lhs_index, 
                           rhs_index, 
                           settings.bar_span )

def deselect_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.unsorted_partition_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.text_color )

def select_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.text_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.selected_color )

def select_squares(squares_canvas, lhs_index, rhs_index):
    select_square( squares_canvas, lhs_index )
    select_square( squares_canvas, rhs_index )
    global previous_indexes
    previous_indexes = [ lhs_index, rhs_index ]

def select_bars(bars_canvas, lhs_index, rhs_index):
    bars_canvas.itemconfig( bars[ lhs_index ], 
                            fill = settings.selected_bar_color )
    bars_canvas.itemconfig( bars[ rhs_index ], 
                            fill = settings.selected_bar_color )
    global previous_indexes
    previous_indexes = [ lhs_index, rhs_index ]

def deselect_squares(squares_canvas):
    deselect_square( squares_canvas, previous_indexes[ 0 ] )
    deselect_square( squares_canvas, previous_indexes[ 1 ] )

def deselect_bars(bars_canvas):
    bars_canvas.itemconfig( bars[ previous_indexes[ 0 ] ], 
                            fill = settings.unsorted_partition_color )
    bars_canvas.itemconfig( bars[ previous_indexes[ 1 ] ], 
                            fill = settings.unsorted_partition_color )

def reset():
    squares.clear()
    values.clear()
    bars.clear()