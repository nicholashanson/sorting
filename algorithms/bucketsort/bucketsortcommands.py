import algorithms.bucketsort.drawbucketsort as drawbucketsort
import time
from algorithms.bucketsort.bucketsort import bucketsort_
import settings

def sort_squares(squares_canvas, data_, speed, number_of_buckets):
    gen = bucketsort_( data_, number_of_buckets )
    length = len( data_ )
    for index, data in enumerate( gen ):
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, index, length, data )
    time.sleep( 5 / speed )
    drawbucketsort.flatten_buckets()
    for index in range( len( data_ ) ):
        drawbucketsort.merge_squares_buckets( squares_canvas, index )
        time.sleep( 5 / speed )
        yield
    drawbucketsort.reset()
    yield

def step_squares(squares_canvas, index, length, data):
    print( data )
    print( index )
    if index == 0:
        drawbucketsort.initialize_buckets( len( data[ 0 ] ) )
    if index < length:
        drawbucketsort.bucket_square( squares_canvas, 
                                      index, 
                                      settings.bucket_colors[ data[ 1 ] ])
        drawbucketsort.add_to_bucket( data[ 1 ], 
                                      index )
    elif data[ 2 ] == True:
        drawbucketsort.swap_squares( squares_canvas, 
                                     data[ 1 ], 
                                     data[ 3 ] )
        drawbucketsort.draw_squares_bubble( squares_canvas, 
                                            data[ 1 ], 
                                            data[ 3 ] )
    else:
        drawbucketsort.remove_squares_bubble( squares_canvas, data[ 1 ] )

def sort_bars(bars_canvas, data_, speed, number_of_buckets):
    gen = bucketsort_( data_, number_of_buckets )
    length = len( data_ )
    for index, data in enumerate( gen ):
        time.sleep( 5 / speed )
        yield
        step_bars( bars_canvas, index, length, data )
    time.sleep( 5 / speed )
    drawbucketsort.flatten_buckets()
    for index in range( len( data_ ) ):
        drawbucketsort.merge_bars_buckets( bars_canvas, index )
        time.sleep( 5 / speed )
        yield
    drawbucketsort.reset()
    yield

def step_bars(bars_canvas, index, length, data):
    print( data )
    print( index )
    if index == 0:
        drawbucketsort.initialize_buckets( len( data[ 0 ] ) )
    if index < length:
        drawbucketsort.bucket_bar( bars_canvas, 
                                      index, 
                                      settings.bucket_colors[ data[ 1 ] ])
        drawbucketsort.add_to_bucket( data[ 1 ], 
                                      index )
    elif data[ 2 ] == True:
        drawbucketsort.swap_bars( bars_canvas, 
                                  data[ 1 ], 
                                  data[ 3 ] )
        drawbucketsort.draw_bars_bubble( bars_canvas, 
                                         data[ 1 ], 
                                         data[ 3 ] )
    else:
        drawbucketsort.remove_bars_bubble( bars_canvas, data[ 1 ] )
