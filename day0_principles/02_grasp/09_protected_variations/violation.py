"""
Protected Variations Violation - GRASP
System bezpośrednio zależny od niestabilnych external APIs
"""

import requests


class WeatherService:
    def get_temperature(self, city):
        # PROBLEM: Bezpośrednie wywołanie external API
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}")
        data = response.json()

        # PROBLEM: Zależność od konkretnej struktury API response
        return data["main"]["temp"]  # Łamie się gdy API się zmieni


class ReportGenerator:
    def __init__(self):
        self.weather_service = WeatherService()

    def generate_weather_report(self, city):
        # PROBLEM: Bezpośrednia dependency na niestabilny API
        try:
            temp = self.weather_service.get_temperature(city)
            return f"Temperature in {city}: {temp}°C"
        except KeyError:
            return "Weather data unavailable"
        # Co jeśli API zmieni format? Albo dodamy inne źródło danych?


class NotificationService:
    def __init__(self):
        self.report_generator = ReportGenerator()

    def send_daily_weather(self, city, user_email):
        report = self.report_generator.generate_weather_report(city)
        # PROBLEM: Cały system zależy od stabilności weather API
        print(f"Sending to {user_email}: {report}")


if __name__ == "__main__":
    service = NotificationService()

    # Symulacja - bez prawdziwego API call
    print("❌ System bezpośrednio zależy od external weather API")
    print("❌ Zmiana formatu API łamie ReportGenerator")
    print("❌ Brak ochrony przed variations w external systems")
