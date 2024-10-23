import unittest
from backend.alerts import WeatherAlert

class TestWeatherAlert(unittest.TestCase):
    def test_check_alert(self):
        alert_system = WeatherAlert(35)
        alert_system.check_alert("Delhi", 36)  # Should not trigger alert
        alert_system.check_alert("Delhi", 34)  # Should not trigger alert
        alert_system.check_alert("Delhi", 36)  # Should trigger alert

if __name__ == '__main__':
    unittest.main()
