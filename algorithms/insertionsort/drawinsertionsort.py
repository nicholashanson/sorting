import settings
import drawing
from globals import squares, values, bars

previous_current_minimum = 0

def swap_squares(squares_canvas, temp):
    drawing.swap_elements( squares_canvas, 
                           squares, 
                           temp, 
                           temp - 1, 
                           settings.square_span,
                           dimensions = 2 )
    drawing.swap_elements( squares_canvas,
                           values,
                           temp,
                           temp - 1,
                           settings.square_span,
                           dimensions = 2 )
    
def swap_bars(bars_canvas, temp):
    drawing.swap_elements( bars_canvas, 
                           bars, 
                           temp, 
                           temp - 1, 
                           settings.bar_span )

def select_sorted_element(canvas, container, index):
    canvas.itemconfig( container[ index ], 
                       fill = settings.sorted_partition_color )

def select_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.text_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.selected_color )

def select_squares(squares_canvas, sorted_upper_bound, temp):
    for index in range( sorted_upper_bound + 1 ):
        if index == temp - 1 or index == temp:
            select_square( squares_canvas, index )
        else:
            select_sorted_element( squares_canvas, 
                                   squares, 
                                   index )  

def select_bars(bars_canvas, sorted_upper_bound, temp):
    for index in range( sorted_upper_bound + 1 ):
        if index == temp - 1 or index == temp:
            bars_canvas.itemconfig( bars[ index ], 
                                    fill = settings.selected_bar_color ) 
        else:
            select_sorted_element( bars_canvas, 
                                   bars, 
                                   index )  

def remove_squares_bubble(squares_canvas, temp):
    select_sorted_element( squares_canvas, squares, temp )
    select_sorted_element( squares_canvas, squares, temp - 1 )

def remove_bars_bubble(bars_canvas, temp):
    select_sorted_element( bars_canvas, bars, temp )
    select_sorted_element( bars_canvas, bars, temp - 1 )

def reset():
    squares.clear()
    values.clear()








    