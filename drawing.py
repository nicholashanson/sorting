import settings
from globals import squares, values, bars

def draw_squares(squares_canvas, data):
    ''' 
    draws all the elements of the square view to the view canvas
    and appends their handles to the corresponding global containers 
    '''
    # reset canvas elements
    squares.clear()
    values.clear()

    for index, data_point in enumerate( data ):
        # draw elements to canvas      
        square, value = draw_square( squares_canvas,
                                     index, 
                                     data_point,
                                     settings.unsorted_partition_color )
        # append elements to global containers
        squares.append( square )
        values.append( value )

def draw_bars(bars_canvas, data):
    ''' 
    draws all the elements of the bars view to the view canvas
    and appends their handle to the global bars container
    '''
    # reset canvas bars container
    bars.clear()

    # if there are less data, shift bars to the right
    x_offset = ( settings.total_elements - len( data ) ) * settings.bar_span

    
    for index, data_point in enumerate( data ): 
        # draw bar to canvas     
        bar = draw_bar( bars_canvas,
                        index, 
                        data_point,
                        x_offset )
        # append bar to canvas bars container
        bars.append( bar )

def draw_bar(bars_canvas, index, data_point, x_offset):
    ''' draws a rectangle to the view canvas and returns its handle '''    
    return bars_canvas.create_rectangle( settings.bars_x_offset + index * settings.bar_span + x_offset,
                                         settings.bars_y_offset,
                                         settings.bars_x_offset + index * settings.bar_span + settings.bar_width + x_offset,
                                         settings.bars_y_offset - settings.y_pixels_per_value * data_point,
                                         fill = settings.unsorted_partition_color )

def swap_elements(canvas, container, lhs_index, rhs_index, element_span,
                  dimensions = 1):
    ''' a generic function that swaps the position of two elements on the view canvas '''
    if ( lhs_index == rhs_index ):
        return
    
    if ( lhs_index > rhs_index ):
        lhs_index, rhs_index = rhs_index, lhs_index

    span = rhs_index - lhs_index

    x = None
    y = None

    if dimensions == 1:
        x = span * element_span
        y = 0
    
    if dimensions == 2:
        lhs_row = lhs_index // settings.elements_per_row
        rhs_row = rhs_index // settings.elements_per_row

        row_span = rhs_row - lhs_row

        y = element_span * ( row_span )
        x = element_span * ( span - row_span * settings.elements_per_row )

    canvas.move( container[ lhs_index ], x, y )
    canvas.move( container[ rhs_index ], -x, -y )
    
    canvas.update_idletasks()
    
    container[ lhs_index ], container[ rhs_index ] = container[ rhs_index ], container[ lhs_index ]


def draw_square(squares_canvas, index, data_point, color):
    ''' 
    draws a square element and its corresponding text widget to the view canvas 
    and returns their handles as a tuple
    '''
    # draw square to contain element
    square = squares_canvas.create_rectangle( ( index % 20 ) * settings.square_span, 
                                              ( index // 20 ) * settings.square_span + settings.square_width, 
                                              ( index % 20 ) * settings.square_span + settings.square_width, 
                                              ( index // 20 ) * settings.square_span,
                                              fill = color )
    # draw value of element inside square
    value = squares_canvas.create_text( ( index % 20 ) * settings.square_span + settings.text_x_offset,
                                        ( index // 20 ) * settings.square_span + settings.square_width - settings.text_y_offset,
                                        text = str( data_point ),
                                        font = ( settings.font, settings.font_size ),
                                        fill = settings.text_color )
    return square, value