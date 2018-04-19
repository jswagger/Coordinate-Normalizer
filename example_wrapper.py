import coordinate_norm


def fix_my_coordinates(original_point):
    print(coordinate_norm.get_new_point(original_point))


def main():
    original_point = {
            'x': 150,
            'y': 740
        }
    fix_my_coordinates(original_point)


if __name__ == '__main__':
    main()
