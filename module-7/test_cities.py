
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

# This test case verifies that the city_country() function correctly formats
# a simple city and country string. It does not test optional arguments like
# population or language. This test ensures backwards compatibility during updates.