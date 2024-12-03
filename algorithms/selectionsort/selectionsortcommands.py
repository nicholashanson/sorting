import algorithms.selectionsort.drawselectionsort as drawselectionsort
import time
from algorithms.selectionsort.selectionsort import selectionsort_

def sort_squares(squares_canvas, data_, speed):
    gen = selectionsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 5 / speed )
    drawselectionsort.extend_sorted_squares( squares_canvas, data[ 1 ] ) 
    drawselectionsort.reset()
    yield

def step_squares(squares_canvas, data):
    print( data )
    drawselectionsort.remove_previous_squares_current_index( squares_canvas,
                                                             data[ 1 ],
                                                             data[ 2 ],
                                                             data[ 3 ] )
    if data[ 4 ] == True:
        if data[ 1 ] != data[ 2 ]:
            drawselectionsort.swap_squares( squares_canvas, 
                                            data[ 1 ], 
                                            data[ 2 ] )
        drawselectionsort.extend_sorted_squares( squares_canvas, 
                                                 data[ 1 ] )
    else:
        drawselectionsort.remove_previous_squares_current_minimum( squares_canvas, data[ 1 ] ) 
        drawselectionsort.select_squares( squares_canvas,  
                                          data[ 2 ], 
                                          data[ 3 ] )

def sort_bars(bars_canvas, data_, speed):
    gen = selectionsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_bars( bars_canvas, data )
    time.sleep( 5 / speed )
    drawselectionsort.extend_sorted_bars( bars_canvas, data[ 1 ] )
    drawselectionsort.reset()
    yield

def step_bars(bars_canvas, data):
    print( data )
    drawselectionsort.remove_previous_bars_current_index( bars_canvas,
                                                          data[ 1 ],
                                                          data[ 2 ],
                                                          data[ 3 ] )
    if data[ 4 ] == True:
        if data[ 1 ] != data[ 2 ]:
            drawselectionsort.swap_bars( bars_canvas, 
                                         data[ 1 ], 
                                         data[ 2 ] )
        drawselectionsort.extend_sorted_bars( bars_canvas, 
                                              data[ 1 ] )
    else:
        drawselectionsort.remove_previous_bars_current_minimum( bars_canvas, data[ 1 ] ) 
        drawselectionsort.select_bars( bars_canvas,  
                                       data[ 2 ], 
                                       data[ 3 ] )