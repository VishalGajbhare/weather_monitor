class WeatherAlert:
    def __init__(self, temperature_threshold):
        self.temperature_threshold = temperature_threshold
        self.previous_temp = {}

    def check_alert(self, city, current_temp):
        if city in self.previous_temp:
            if (current_temp > self.temperature_threshold and
                self.previous_temp[city] > self.temperature_threshold):
                print(f"ALERT: {city} has exceeded {self.temperature_threshold}°C!")
        
        self.previous_temp[city] = current_temp
