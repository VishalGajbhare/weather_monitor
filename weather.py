import requests
import time
from datetime import datetime
from config import API_KEY, CITIES, UPDATE_INTERVAL
from database import init_db, insert_daily_summary

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def process_weather_data(data):
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    condition = data['weather'][0]['main']
    timestamp = data['dt']
    
    return temp, feels_like, condition, timestamp

def run_weather_monitor():
    init_db()
    while True:
        for city in CITIES:
            data = fetch_weather(city)
            if data.get('cod') != 200:
                print(f"Failed to get data for {city}: {data.get('message')}")
                continue

            temp, feels_like, condition, timestamp = process_weather_data(data)
            date_str = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

            # Here you can implement rollup logic to calculate daily aggregates
            # For simplicity, let's assume we're storing data daily.
            insert_daily_summary(city, date_str, temp, temp, temp, condition)

        time.sleep(UPDATE_INTERVAL)
