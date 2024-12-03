def insertionsort_(data):
    
    sorted_upper_bound = 1
    temp = None

    while sorted_upper_bound < len(data):
        temp = sorted_upper_bound
        while temp > 0:
            yield data, sorted_upper_bound, temp, False
            if data[ temp ] < data[ temp - 1 ]:
                yield data, sorted_upper_bound, temp, True
                data[ temp ], data[ temp - 1 ] = data[ temp - 1], data[ temp ]
                temp -= 1
            else:
                break
        sorted_upper_bound += 1
    yield data, sorted_upper_bound, temp, False