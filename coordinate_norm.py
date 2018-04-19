#-------------------------------------------------------------------------------
# Name:         Coordinate Normalizer
# Purpose:      Corrects latitude and longitude decimal degree values to match a -90 to 90 and -180 to 180 format.
#               Takes an object containing 'x' and 'y' properties, with values as doubles.
#
# Dependencies: none
#
# Author:      jswagger
#
# Created:     04/18/2018
# Licence:     MIT


def adjust_latitude(value):
    if value > 90.0 or value < -90.0:
        return -(((value + 90) % 180) - 90)
    return((value + 90) % 180) - 90


def adjust_longitude(value):
    return((value + 180) % 360) - 180


def get_new_point(original_point):
    new_x = adjust_longitude(original_point['x'])
    new_y = adjust_latitude(original_point['y'])
    new_point = type('Point', (object,), {
        'x': new_x,
        'y': new_y
    })
    return new_point


def get_object():
    return {
            'x': 55,
            'y': 122
        }


def main():
    original_point = get_object()
    new_point = get_new_point(original_point)
    return new_point


if __name__ == '__main__':
    main()
