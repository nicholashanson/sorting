import settings
from globals import squares, values, bars

def draw_squares(squares_canvas, data):
    squares.clear()
    values.clear()
    for index, data_point in enumerate( data ):      
        square, value = draw_square( squares_canvas,
                                     index, 
                                     data_point,
                                     settings.unsorted_partition_color )
        squares.append( square )
        values.append( value )
    print( len( squares ) )

def draw_bars(bars_canvas, data):
    x_offset = ( settings.total_elements - len( data ) ) * settings.bar_span 
    bars.clear()
    for index, data_point in enumerate( data ):      
        bar = draw_bar( bars_canvas,
                        index, 
                        data_point,
                        x_offset )
        bars.append( bar )

def draw_bar(bars_canvas, index, data_point, x_offset):    
    return bars_canvas.create_rectangle( settings.bars_x_offset + index * settings.bar_span + x_offset,
                                         settings.bars_y_offset,
                                         settings.bars_x_offset + index * settings.bar_span + settings.bar_width + x_offset,
                                         settings.bars_y_offset - settings.y_pixels_per_value * data_point,
                                         fill = settings.unsorted_partition_color )

def swap_elements(canvas, container, lhs_index, rhs_index, element_span,
                  dimensions = 1):
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