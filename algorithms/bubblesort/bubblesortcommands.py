import algorithms.bubblesort.drawbubblesort as drawbubblesort
import time
from algorithms.bubblesort.bubblesort import bubblesort_

def sort_squares(squares_canvas, data_, speed):
    gen = bubblesort_( data_ )
    drawbubblesort.draw_squares_bubble( squares_canvas, 0 )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 5 / speed )
    drawbubblesort.remove_squares_bubble( squares_canvas )
    drawbubblesort.reset()
    yield

def sort_bars(bars_canvas, data_, speed):
    gen = bubblesort_( data_ )
    drawbubblesort.draw_bars_bubble( bars_canvas, 0 )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_bars( bars_canvas, data )
    time.sleep( 5 / speed )
    drawbubblesort.remove_bars_bubble( bars_canvas )
    drawbubblesort.reset()
    yield

def step_bars(bars_canvas, data):
    drawbubblesort.draw_bars_bubble( bars_canvas, 
                                     data[ 1 ]  )
    if ( data[ 2 ] == True ):
        drawbubblesort.swap_bars( bars_canvas, 
                                  data[ 1 ] )

def step_squares(squares_canvas, data):
    drawbubblesort.draw_squares_bubble( squares_canvas, 
                                        data[ 1 ]  )
    print( data )
    if ( data[ 2 ] == True ):
        drawbubblesort.swap_squares( squares_canvas, 
                                     data[ 1 ] )