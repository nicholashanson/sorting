import algorithms.quicksort.drawquicksort as drawquicksort
import time
from algorithms.quicksort.quicksort import quicksort_

def sort_squares(squares_canvas, data_, speed):
    gen = quicksort_( data_, 0, len( data_ ) - 1 )
    for index, data in enumerate( gen ):
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, index, data )
    time.sleep( 5 / speed )
    drawquicksort.deselect_squares( squares_canvas )
    drawquicksort.reset()
    yield

def sort_bars(bars_canvas, data_, speed):
    gen = quicksort_( data_, 0, len( data_ ) - 1 )
    for index, data in enumerate( gen ):
        time.sleep( 5 / speed )
        yield
        step_bars( bars_canvas, index, data )
    time.sleep( 5 / speed )
    drawquicksort.deselect_bars( bars_canvas )
    drawquicksort.reset()
    yield

def step_squares(squares_canvas, index, data):
    print( data )
    if index != 0:
        drawquicksort.deselect_squares( squares_canvas )
    drawquicksort.select_squares( squares_canvas, 
                                  data[ 1 ], 
                                  data[ 2 ] )
    if data[ 3 ] == True:
        drawquicksort.swap_squares( squares_canvas, 
                                    data[ 1 ], 
                                    data[ 2 ] )
        
def step_bars(bars_canvas, index, data):
    print( data )
    if index != 0:
        drawquicksort.deselect_bars( bars_canvas )
    drawquicksort.select_bars( bars_canvas, 
                               data[ 1 ], 
                               data[ 2 ] )
    if data[ 3 ] == True:
        drawquicksort.swap_bars( bars_canvas, 
                                 data[ 1 ], 
                                 data[ 2 ] )
    
    