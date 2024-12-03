def bubblesort_(data):
        
    # checkers for sorting
    sorted = False
    # set to 1 on each pass with swap
    sorting_flag = 0
    
    while sorted == False:
        for i in range( len ( data ) - 1 ):
            # False: no swap
            yield data, i, False
            # perform a swap
            if data[ i ] > data[ i + 1 ]:
                # True: swap
                yield data, i, True
                data[ i ], data[ i + 1 ] = data[ i + 1 ], data[ i ]
                # still not sorted
                sorting_flag = 1

        # no swaps this pass
        if sorting_flag == 0:
            sorted = True
        else:
            # reset for next pass
            sorting_flag = 0

        
