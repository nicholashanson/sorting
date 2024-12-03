def selectionsort_(data):

    current_minimum = 0
    current_index = 0
    partition_upper_bound = 0

    while partition_upper_bound < len(data) - 1:
        while current_index < len(data):
            yield data, partition_upper_bound, current_minimum, current_index, False
            if data[ current_index ] < data[ current_minimum ]:
                current_minimum = current_index
            current_index += 1
        yield data, partition_upper_bound, current_minimum, current_index - 1, True
        data[ partition_upper_bound], data[ current_minimum ] = data[ current_minimum ], data[ partition_upper_bound ]
        partition_upper_bound += 1
        current_minimum = current_index = partition_upper_bound
    yield data, partition_upper_bound, current_minimum, current_index, False