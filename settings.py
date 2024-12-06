# square dimensions
square_width = 40
square_gap = 5
square_span = square_width + square_gap
elements_per_row = 20

# widget dimensions
# main window width
root_x = 900
# main window height
root_y = 500
status_bar_height = 25
# portion of main window occupied by the options frame
options_frame_rel_width = 1 / 3
options_frame_width = root_x * options_frame_rel_width
options_frame_height = root_y - status_bar_height
view_container_frame_height = options_frame_height
# start drawing view container from this x position
view_container_x_offset = options_frame_width
# distance in pixels from the top of the main window
# to the top of the status bar
status_bar_y_offset = root_y - status_bar_height
view_container_frame_width = root_x - options_frame_width
view_canvas_width = 20 * square_span - square_gap
view_canvas_height = 10 * square_span - square_gap

# bar dimensions
bar_width = 3
bar_gap = 1
bar_span = bar_width + bar_gap
# determines the height of the bar
y_pixels_per_value = 1
# start drawing bars from this x position
# on the canvas
bars_x_offset = 50
# bottom edge of bar is at this y position
# on the canvas
bars_y_offset = 400

# text
font = 'Arial'
font_size = 12
text_color = 'white'
text_x_offset = square_width / 2
text_y_offset = square_width / 2

# colors
sorted_partition_color = 'green'
unsorted_partition_color = 'blue'
selected_bar_color = 'white'
# bar color
bar_fill = 'blue'
# selection sort
current_minimum_color = 'red'
current_index_color = 'yellow'
# bucketsort squares view
bucket_colors = [
    'dark salmon',
    'salmon',
    'light salmon',
    'orange',
    'dark orange',
    'coral',
    'light coral',
    'tomato',
    'orange red',
    'red'
]

total_elements = 200