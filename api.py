from weather import run_weather_monitor
from alerts import WeatherAlert
from config import UPDATE_INTERVAL

if __name__ == "__main__":
    weather_alert = WeatherAlert(35)  # Example threshold
    run_weather_monitor()
