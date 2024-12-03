frame_relief = 'raised'

border_width = 3

y_pixels_per_value = 1

root_x = 900
root_y = 500
status_bar_height = 25
options_frame_rel_width = 1 / 3
options_frame_width = root_x * options_frame_rel_width
options_frame_height = root_y - status_bar_height
view_container_frame_height = options_frame_height
view_container_x_offset = options_frame_width
status_bar_y_offset = root_y - status_bar_height
view_container_frame_width = root_x - options_frame_width

# square dimensions
square_width = 40
square_gap = 5
square_span = square_width + square_gap

elements_per_row = 20
total_elements = 200

view_canvas_width = 20 * square_span - square_gap
view_canvas_height = 10 * square_span - square_gap

# bar dimensions
bar_width = 3
bar_gap = 1
bar_span = bar_width + bar_gap
bars_x_offset = 50
bars_y_offset = 400

# bar color
bar_fill = 'blue'

# text
font = 'Arial'
font_size = 12
text_color = 'white'
text_x_offset = square_width / 2
text_y_offset = square_width / 2

sorted_partition_color = 'green'
unsorted_partition_color = 'blue'

# selection sort
current_minimum_color = 'red'
current_index_color = 'yellow'

selected_color = 'blue'

selected_bar_color = 'white'

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