import coordinate_norm
import unittest


class CoordinateNormalizerUnitTests(unittest.TestCase):
    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_1(self):
        fake_object = {
            'x': 190,
            'y': 240
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, -170)
        self.assertEqual(corrected_latitude, -60)

    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_2(self):
        fake_object = {
            'x': -210,
            'y': 120
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, 150)
        self.assertEqual(corrected_latitude, 60)

    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_3(self):
        fake_object = {
            'x': 720,
            'y': -10
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, 0)
        self.assertEqual(corrected_latitude, -10)

    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_4(self):
        fake_object = {
            'x': -750,
            'y': 0
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, -30)
        self.assertEqual(corrected_latitude, 0)

    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_5(self):
        fake_object = {
            'x': -890,
            'y': -100
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, -170)
        self.assertEqual(corrected_latitude, -80)

    def test_when_correcting_latitude_and_longitude_should_return_valid_value_case_6(self):
        fake_object = {
            'x': 920,
            'y': 180
        }
        corrected_longitude = coordinate_norm.adjust_longitude(fake_object['x'])
        corrected_latitude = coordinate_norm.adjust_latitude(fake_object['y'])
        self.assertEqual(corrected_longitude, -160)
        self.assertEqual(corrected_latitude, 0)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
