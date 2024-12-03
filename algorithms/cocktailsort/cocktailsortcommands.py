import algorithms.cocktailsort.drawcocktailsort as drawcocktailsort
import time
from algorithms.cocktailsort.cocktailsort import cocktailsort_

def sort_squares(squares_canvas, data_, speed):
    gen = cocktailsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 5 / speed )
    drawcocktailsort.remove_squares_bubble( squares_canvas ) 
    drawcocktailsort.reset()
    yield

def step_squares(squares_canvas, data):
    drawcocktailsort.draw_squares_bubble( squares_canvas, data[ 1 ], data[ 2 ] )
    print( data )
    if ( data[ 3 ] == True ):
        drawcocktailsort.swap_squares( squares_canvas, data[ 1 ], data[ 2 ] )

def sort_bars(bars_canvas, data_, speed):
    gen = cocktailsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_bars( bars_canvas, data )
    time.sleep( 5 / speed )
    drawcocktailsort.remove_bars_bubble( bars_canvas )
    drawcocktailsort.reset()
    yield

def step_bars(bars_canvas, data):
    drawcocktailsort.draw_bars_bubble( bars_canvas, data[ 1 ], data[ 2 ] )
    print( data )
    if ( data[ 3 ] == True ):
        drawcocktailsort.swap_bars( bars_canvas, data[ 1 ], data[ 2 ] )