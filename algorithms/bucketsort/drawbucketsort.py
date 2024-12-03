import settings
import drawing
from globals import squares, values, bars

buckets = None
flat_buckets = None

def swap_squares(squares_canvas, bucket_index, temp):
    rhs_square_index = buckets[ bucket_index ][ temp ]
    lhs_square_index = buckets[ bucket_index ][ temp - 1 ]
    drawing.swap_elements( squares_canvas, 
                           squares, 
                           lhs_square_index, 
                           rhs_square_index, 
                           settings.square_span,
                           dimensions = 2 )
    drawing.swap_elements( squares_canvas,
                           values,
                           lhs_square_index,
                           rhs_square_index,
                           settings.square_span,
                           dimensions = 2 ) 
    
def swap_bars(bars_canvas, bucket_index, temp):
    rhs_bar_index = buckets[ bucket_index ][ temp ]
    lhs_bar_index = buckets[ bucket_index ][ temp - 1 ]
    drawing.swap_elements( bars_canvas, 
                           bars, 
                           lhs_bar_index, 
                           rhs_bar_index, 
                           settings.bar_span ) 

def bucket_square(squares_canvas, index, color):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = color )
    
def bucket_bar(bars_canvas, index, color):
    bars_canvas.itemconfig( bars[ index ], 
                            fill = color )
    
def deselect_square(squares_canvas, index, color):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.text_color )
    
def initialize_buckets(length):
    global buckets
    buckets = [ [] for _ in range( length ) ]

def add_to_bucket(bucket_index, element_index):
    buckets[ bucket_index ].append( element_index )

def select_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.text_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.selected_color )

def draw_squares_bubble(squares_canvas, bucket_index, temp):
    rhs_index = buckets[ bucket_index ][ temp ]
    lhs_index = buckets[ bucket_index ][ temp - 1 ]
    select_square( squares_canvas, rhs_index )
    select_square( squares_canvas, lhs_index )  

def draw_bars_bubble(bars_canvas, bucket_index, temp):
    rhs_index = buckets[ bucket_index ][ temp ]
    lhs_index = buckets[ bucket_index ][ temp - 1 ]
    bars_canvas.itemconfig( bars[ lhs_index ], 
                            fill = settings.text_color )
    bars_canvas.itemconfig( bars[ rhs_index ], 
                            fill = settings.text_color )

def remove_squares_bubble(squares_canvas, bucket_index):
    for square_index in buckets[ bucket_index ]:
        deselect_square( squares_canvas, 
                         square_index, 
                         settings.bucket_colors[ bucket_index ] )

def remove_bars_bubble(bars_canvas, bucket_index):
    for bar_index in buckets[ bucket_index ]:
        bars_canvas.itemconfig( bars[ bar_index ], 
                                fill = settings.bucket_colors[ bucket_index ] )
        
def flatten_buckets():
    global flat_buckets
    flat_buckets = sum( buckets, [])

def merge_squares_buckets(squares_canvas, index):
    if flat_buckets[ index ] != index:  
        drawing.swap_elements( squares_canvas, 
                               squares, 
                               index, 
                               flat_buckets[ index ], 
                               settings.square_span,
                               dimensions = 2 )
        drawing.swap_elements( squares_canvas, 
                               values, 
                               index, 
                               flat_buckets[ index ], 
                               settings.square_span,
                               dimensions = 2 )
        temp = flat_buckets[ index ]
        other_index = flat_buckets.index( index )
        flat_buckets[ other_index ] = temp
        flat_buckets[ index ] = index 

def merge_bars_buckets(bars_canvas, index):
    if flat_buckets[ index ] != index:  
        drawing.swap_elements( bars_canvas, 
                               bars, 
                               index, 
                               flat_buckets[ index ], 
                               settings.bar_span )
        temp = flat_buckets[ index ]
        other_index = flat_buckets.index( index )
        flat_buckets[ other_index ] = temp
        flat_buckets[ index ] = index 

def reset():
    global buckets
    global flat_buckets
    squares.clear()
    values.clear()
    bars.clear()
    buckets = None
    flat_buckets = None









    