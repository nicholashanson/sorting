def cocktailsort_(data):

    sorted = False
    sorting_flag = 0
        
    while sorted == False:
        for i in range( len( data ) - 1 ):
            yield data, i, i + 1, False
            if data[ i ] > data[ i + 1 ]:
                yield data, i, i + 1, True
                data[ i ], data[ i + 1 ] = data[ i + 1 ], data[ i ]
                sorting_flag = 1                

        i = len( data ) - 1

        while i > 0:
            yield data, i, i - 1, False
            if data[ i - 1 ] > data[ i ]:
                yield data, i, i - 1, True
                data[ i ], data[ i - 1 ] = data[ i - 1 ], data[ i ]
                sorting_flag = 1

            i -= 1

        if sorting_flag == 0:
            sorted = True
        else:
            sorting_flag = 0