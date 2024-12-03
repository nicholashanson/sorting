import tkinter as tk
root = tk.Tk()
import random
from tkinter import messagebox
import drawing
import settings
import algorithms.bubblesort.bubblesortcommands as bubblesortcommands
import algorithms.cocktailsort.cocktailsortcommands as cocktailsortcommands
import algorithms.selectionsort.selectionsortcommands as selectionsortcommands
import algorithms.insertionsort.insertionsortcommands as insertionsortcommands
import algorithms.quicksort.quicksortcommands as quicksortcommands
import algorithms.bucketsort.bucketsortcommands as bucketsortcommands
from globals import squares, values

root.geometry( str( settings.root_x ) + 'x' + str ( settings.root_y ) ) 

options_frame = tk.Frame( root, 
                          bg = 'gainsboro' )
options_frame.place( width = settings.options_frame_width, 
                     height = settings.options_frame_height )

view_container_frame = tk.Frame( root, bg = 'gainsboro' )
view_container_frame.place( x = settings.view_container_x_offset, 
                            height = settings.view_container_frame_height )

status_bar = tk.Frame( root, 
                       bg = 'gainsboro', 
                       relief = 'raised', 
                       border = 1 )
status_bar.place( y = settings.status_bar_y_offset, 
                  width = settings.root_x, 
                  height = settings.status_bar_height )

view_frame = tk.Frame( view_container_frame,
                       width = settings.view_container_frame_width - 20,
                       height = settings.view_container_frame_height - 20, 
                       border = 1,
                       relief = 'sunken',
                       background = 'white smoke' )
view_frame.place( x = 10, y = 10 )

algorithm_frame = tk.Frame( options_frame, 
                            width = settings.options_frame_width - 20, 
                            height = 100 )

speed_frame = tk.Frame( options_frame, 
                        width = settings.options_frame_width - 20, 
                        height = 100 )

speed_label = tk.Label( speed_frame, text = "Speed:" )
speed_label.place( x = 10, y = 10 )

generator_frame = tk.Frame( options_frame, 
                            width = settings.options_frame_width - 20, 
                            height = 200,
                            padx = 10, 
                            pady = 10 )
generator_frame.place( in_ = speed_frame, 
                       relx = 0.0, 
                       x = 0, 
                       rely = 1.0, 
                       y = 10 )

mimimum_value_label = tk.Label( generator_frame, 
                                text = 'Minimum value:' )
mimimum_value_label.pack()

mimimum_value_slide = tk.Scale( generator_frame, 
                                from_= 0, 
                                to = 200, 
                                orient = tk.HORIZONTAL )
mimimum_value_slide.set( 20 )
mimimum_value_slide.pack()

maximum_value_label = tk.Label( generator_frame, 
                                text = 'Maximum value:' )
maximum_value_label.pack()

maximum_value_slide = tk.Scale( generator_frame, 
                                from_= 0, 
                                to = 200, 
                                orient = tk.HORIZONTAL )
maximum_value_slide.set( 200 )
maximum_value_slide.pack()

number_of_elements_label = tk.Label( generator_frame, text = 'Number of elements:' )
number_of_elements_label.pack()

number_of_elements_slide = tk.Scale( generator_frame, 
                                     from_= 0, 
                                     to = 200, 
                                     orient = tk.HORIZONTAL )
number_of_elements_slide.set( 20 )
number_of_elements_slide.pack()

data = []

view_options = [ 
        'Bars', 
        'Squares'
] 

algorithm_options = [ 
    'Quicksort', 
    'Bubblesort',
    'Insertionsort',
    'Selectionsort',
    'Cocktailsort',
    'Bucketsort'
]


selected_view = tk.StringVar()   
selected_view.set( 'Squares' ) 

bars_canvas = tk.Canvas( view_frame, bd = -2,
                         width = settings.view_canvas_width, 
                         height = settings.view_canvas_height )
squares_canvas = tk.Canvas( view_frame, bd = -2,
                            width = settings.view_canvas_width, 
                            height = settings.view_canvas_height )

view_canvas = squares_canvas

view_canvas.place( x = ( settings.view_container_frame_width - 20 ) / 2,
                   y = ( settings.view_container_frame_height - 20 ) / 2,
                   anchor = 'center' )


number_of_buckets_slide = tk.Scale( algorithm_frame, 
                                    from_ = 1, 
                                    to = 20, 
                                    orient = tk.HORIZONTAL )

number_of_buckets_label = tk.Label( algorithm_frame, 
                                    text = 'Number of buckets:' )

def choose_view(view):
    global view_canvas
    view_canvas.delete( 'all' )
    view_canvas.place_forget()
    if ( view == 'Bars' ):
        view_canvas = bars_canvas
        drawing.draw_bars( view_canvas, data )
    else:
        view_canvas = squares_canvas
        drawing.draw_squares( view_canvas, data )
    view_canvas.place( x = ( root.winfo_width() - root.winfo_width() * settings.options_frame_rel_width - 20 ) / 2,
                       y = ( root.winfo_height() - settings.status_bar_height - 20 ) / 2,
                       anchor = 'center' )

view = tk.OptionMenu( view_frame, 
                      selected_view, 
                      *view_options, 
                      command = choose_view ) 
view.place( x = settings.view_container_frame_width - 30, 
            y = 10, 
            anchor = 'ne' )

gen = None

partially_sorted = tk.IntVar()
partially_sorted_checkbox = tk.Checkbutton( generator_frame, 
                                            text = 'Partiallly sorted', 
                                            variable = partially_sorted )
partially_sorted_checkbox.pack()

def partially_sort():
    pass

def generate():
    # reset
    sort_button[ 'state' ] = 'normal'
    view_canvas.delete( 'all' )
    data.clear()
    
    # used to generate random data
    number_of_elements = number_of_elements_slide.get()
    minimum_value = mimimum_value_slide.get()
    maximum_value = maximum_value_slide.get()

    # minimum can't be less than maximum
    if minimum_value > maximum_value:
        messagebox.showerror('Error', 
                             'Minimum value is greater than maximum value.')
        
    # generate random data
    for _ in range( number_of_elements ):
        data.append( random.randint( minimum_value, maximum_value ) )

    if partially_sorted.get() == 1:
        partially_sort()

    # draw data
    if selected_view.get() == 'Squares':
        drawing.draw_squares( view_canvas, data )
    else: 
        drawing.draw_bars( view_canvas, data )

generate_button = tk.Button( generator_frame, 
                             text = 'Generate', 
                             command = generate )
generate_button.pack( pady = (5, 0) )

# full-screen main window
root.state( 'zoomed' )

algorithm_label = tk.Label( algorithm_frame, 
                            text = 'Algorithm:' )
algorithm_label.place( x = 10, y = 10 )

def handle_algorithm_selection(algorithm):
    if algorithm == 'Bucketsort':
        number_of_buckets_slide.place( x = settings.options_frame_width - 30, 
                                       y = 50,
                                       anchor = 'ne' )
        number_of_buckets_label.place( x = 10, y = 50 )
    else:
        number_of_buckets_slide.place_forget()
        number_of_buckets_label.place_forget()

selected_algorithm = tk.StringVar()
selected_algorithm.set( 'Quicksort' )
algorithm = tk.OptionMenu( algorithm_frame, 
                           selected_algorithm, 
                           *algorithm_options,
                           command = handle_algorithm_selection )

algorithm.place( x = settings.options_frame_width - 30, 
                 y = 10, 
                 anchor = 'ne' )
algorithm_frame.place( x = 10, y = 10 )

def handle_sort():
    global gen
    sort_button[ 'state' ] = 'disabled'
    speed = speed_slide.get()
    current_view = selected_view.get()
    number_of_buckets = number_of_buckets_slide.get()
    match selected_algorithm.get():
        case 'Bubblesort':
            if current_view == 'Squares':
                gen = bubblesortcommands.sort_squares( view_canvas, 
                                                       data, 
                                                       speed )
            else:
                gen = bubblesortcommands.sort_bars( view_canvas,
                                                    data,
                                                    speed )
        case 'Cocktailsort':
            if current_view == 'Squares':    
                gen = cocktailsortcommands.sort_squares( view_canvas,
                                                         data, 
                                                         speed )
            else:
                gen = cocktailsortcommands.sort_bars( view_canvas, 
                                                      data,
                                                      speed )
        case 'Selectionsort':
            if current_view == 'Squares':
                gen = selectionsortcommands.sort_squares( view_canvas, 
                                                          data, 
                                                          speed )
            else:
                gen = selectionsortcommands.sort_bars( view_canvas,
                                                       data,
                                                       speed )
        case 'Insertionsort':
            if current_view == 'Squares':
                gen = insertionsortcommands.sort_squares( view_canvas, 
                                                          data, 
                                                          speed )
            else:
                gen = insertionsortcommands.sort_bars( view_canvas,
                                                       data,
                                                       speed )
        case 'Quicksort':
            if current_view == 'Squares':
                gen = quicksortcommands.sort_squares( squares_canvas, 
                                                      data, 
                                                      speed )
            else:
                gen = quicksortcommands.sort_bars( bars_canvas,
                                                   data,
                                                   speed )
        case 'Bucketsort':
            if current_view == 'Squares':
                gen = bucketsortcommands.sort_squares( view_canvas, 
                                                       data, 
                                                       speed,
                                                       number_of_buckets )
            else:
                gen = bucketsortcommands.sort_bars( view_canvas, 
                                                    data, 
                                                    speed,
                                                    number_of_buckets )
        case _: 
            pass

sort_button = tk.Button( view_frame, 
                         text = 'Sort', 
                         command = handle_sort )
sort_button.place( x = 10, 
                   y = settings.status_bar_y_offset - 30, 
                   anchor = 'sw' )

speed_frame.place( in_ = algorithm_frame, 
                   rely = 1.0, 
                   y = 10 , 
                   relx = 0.0, 
                   x = 0 )

speed_slide = tk.Scale( speed_frame, 
                         from_= 0, 
                         to = 200, 
                         orient = tk.HORIZONTAL )
speed_slide.place( x = settings.options_frame_width - 30, 
                   y = 10, 
                   anchor = 'ne' )
speed_slide.set( 200 )

def draw(this_window_width, this_window_height):
    options_frame.place( width = this_window_width * settings.options_frame_rel_width, 
                         height = this_window_height - settings.status_bar_height )
    
    view_container_frame.place( x = this_window_width * settings.options_frame_rel_width, 
                                width = this_window_width - this_window_width * settings.options_frame_rel_width,
                                height = this_window_height - settings.status_bar_height )
    
    status_bar.place( y = this_window_height - settings.status_bar_height, 
                      relwidth = 1 )
    
    view_frame.place( width = this_window_width - this_window_width * settings.options_frame_rel_width - 20,
                      height = this_window_height - settings.status_bar_height - 20  )
    
    view.place( x = this_window_width - ( this_window_width * settings.options_frame_rel_width ) - 30, 
                y = 10, 
                anchor = 'ne' )
    
    sort_button.place( x = 10, y = this_window_height - settings.status_bar_height - 30, anchor = 'sw' )

    view_canvas.place( x = ( this_window_width - this_window_width * settings.options_frame_rel_width  - 20 ) / 2,
                       y = ( this_window_height - settings.status_bar_height - 20 ) / 2,
                       anchor = 'center' )

last_window_width = this_window_width = root.winfo_width()
last_window_height = this_window_height = root.winfo_height()

draw( this_window_width, this_window_height )

while True:

    if last_window_width != this_window_width or last_window_height != this_window_height:
        draw( this_window_width, this_window_height )

    last_window_width = this_window_width
    last_window_height = this_window_height

    this_window_width = root.winfo_width()
    this_window_height = root.winfo_height()

    if gen != None:
        for i in gen:
            root.update()
            gen = None
    else: 
        root.update()





