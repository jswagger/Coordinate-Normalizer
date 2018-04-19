# Coordinate-Normalizer
Corrects latitude and longitude decimal degree values to match a -90 to 90 and -180 to 180 format.
Takes an object containing 'x' and 'y' properties, with values as doubles.

Check out the example_wrapper for an example on common use. 

    import coordinate_norm
    
    original_point = {
            'x': 55,
            'y': 122
        }
    revised_point = coordinate_norm.get_new_point(original_point)
