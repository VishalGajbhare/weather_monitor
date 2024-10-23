import unittest
from backend.weather import process_weather_data

class TestWeatherProcessing(unittest.TestCase):
    def test_process_weather_data(self):
        sample_data = {
            'main': {'temp': 30, 'feels_like': 28},
            'weather': [{'main': 'Clear'}],
            'dt': 1635012800  # Sample Unix timestamp
        }
        temp, feels_like, condition, timestamp = process_weather_data(sample_data)
        self.assertEqual(temp, 30)
        self.assertEqual(condition, 'Clear')

if __name__ == '__main__':
    unittest.main()
