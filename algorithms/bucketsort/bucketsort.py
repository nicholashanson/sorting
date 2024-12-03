from algorithms.insertionsort.insertionsort import insertionsort_

def bucketsort_(data, number_of_buckets = 10):

    lower_bound = min(data)
    upper_bound = max(data)
    range_ = upper_bound - lower_bound

    # less than an average of two items per bucket
    # cut the number of buckets in half
    if ( len( data ) / 2 < number_of_buckets ):
        number_of_buckets = int( len(data) / 2 )

    bucket_width = range_ / number_of_buckets

    # bucket definitions: (index, lower_bound, upper_bound)
    bucket_ranges = []

    # lists of items in each bucket
    buckets = [ [] for _ in range( number_of_buckets ) ]

    for i in range( number_of_buckets - 1 ):
        bucket_ranges.append( tuple([ 
            i, 
            lower_bound + i * bucket_width,
            lower_bound + ( i + 1 ) * bucket_width ]) )
        
    bucket_ranges.append( tuple([
            number_of_buckets - 1, 
            lower_bound + ( number_of_buckets - 1 ) * bucket_width,
            upper_bound ]) )
    
    # split the data into buckets
    for data_point in data:
        for bucket in bucket_ranges:
            if data_point >= bucket[ 1 ] and data_point < bucket[ 2 ]:
                buckets[ bucket[ 0 ] ].append( data_point )
                yield buckets, bucket[ 0 ]
                break
            if bucket[ 0 ] == number_of_buckets - 1:
                buckets[ number_of_buckets - 1 ].append( data_point )
                yield buckets, bucket[ 0 ]  

    # sort each bucket
    for bucket_index, bucket in enumerate( buckets ):
        gen = insertionsort_( bucket ) 
        for i in gen:
            yield buckets, bucket_index, i[ 3 ], i[ 2 ]



