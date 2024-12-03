import settings
import drawing
from globals import squares, values, bars

previous_current_minimum = None

def swap_squares(squares_canvas, partition_upper_bound, current_minimum):
    drawing.swap_elements( squares_canvas, 
                           squares, 
                           partition_upper_bound, 
                           current_minimum, 
                           settings.square_span,
                           dimensions = 2)
    drawing.swap_elements( squares_canvas,
                           values,
                           partition_upper_bound,
                           current_minimum,
                           settings.square_span,
                           dimensions = 2 )

def swap_bars(bars_canvas, partition_upper_bound, current_minimum):
    drawing.swap_elements( bars_canvas, 
                           bars, 
                           partition_upper_bound, 
                           current_minimum, 
                           settings.bar_span)

def extend_sorted_squares(squares_canvas, partition_upper_bound):
    squares_canvas.itemconfig( squares[ partition_upper_bound ],
                               fill = settings.sorted_partition_color )
    
def extend_sorted_bars(bars_canvas, partition_upper_bound):
    bars_canvas.itemconfig( bars[ partition_upper_bound ],
                            fill = settings.sorted_partition_color )
    
def remove_previous_squares_current_index(squares_canvas, partition_upper_bound, current_minimum, current_index):
    if current_minimum == current_index - 1 or current_index == 0:
        return
    elif partition_upper_bound == current_index:
        squares_canvas.itemconfig( squares[ -1 ],
                                   fill = settings.unsorted_partition_color )
    else:
        squares_canvas.itemconfig( squares[ current_index - 1],
                                   fill = settings.unsorted_partition_color )
    
def remove_previous_bars_current_index(bars_canvas, partition_upper_bound, current_minimum, current_index):
    if current_minimum == current_index - 1 or current_index == 0:
        return
    elif partition_upper_bound == current_index:
        bars_canvas.itemconfig( bars[ -1 ],
                                fill = settings.unsorted_partition_color )
    else:
        bars_canvas.itemconfig( bars[ current_index - 1],
                                fill = settings.unsorted_partition_color )

def remove_previous_squares_current_minimum(squares_canvas, partition_upper_bound):
    if previous_current_minimum == None:
        return
    if previous_current_minimum < partition_upper_bound:
        return
    squares_canvas.itemconfig( squares[ previous_current_minimum ],
                               fill = settings.unsorted_partition_color )
    
def remove_previous_bars_current_minimum(bars_canvas, partition_upper_bound):
    if previous_current_minimum == None:
        return
    if previous_current_minimum < partition_upper_bound:
        return
    bars_canvas.itemconfig( bars[ previous_current_minimum ],
                            fill = settings.unsorted_partition_color )
    
def select_squares(squares_canvas, current_minimum, current_index):
    squares_canvas.itemconfig( squares[ current_index ],
                               fill = settings.current_index_color )
    squares_canvas.itemconfig( squares[ current_minimum ],
                               fill = settings.current_minimum_color )
    global previous_current_minimum
    previous_current_minimum = current_minimum

def select_bars(bars_canvas, current_minimum, current_index):
    bars_canvas.itemconfig( bars[ current_index ],
                            fill = settings.current_index_color )
    bars_canvas.itemconfig( bars[ current_minimum ],
                            fill = settings.current_minimum_color )
    global previous_current_minimum
    previous_current_minimum = current_minimum

def clean_up(squares_canvas):
    squares_canvas.itemconfig( squares[ -1], 
                               fill = settings.sorted_partition_color )

def clean_up(bars_canvas):
    bars_canvas.itemconfig( squares[ -1], 
                            fill = settings.sorted_partition_color )

def reset():
    squares.clear()
    values.clear()
    bars.clear()