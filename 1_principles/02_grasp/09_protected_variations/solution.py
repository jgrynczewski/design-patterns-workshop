"""
Protected Variations Solution - GRASP
Ochrona przed zmianami przez stable interfaces
"""

from abc import ABC, abstractmethod


# Stable internal model - chroni przed external changes
class WeatherData:
    def __init__(self, temperature, humidity, condition):
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition


# Interface chroni przed zmianami w external APIs
class WeatherProvider(ABC):
    @abstractmethod
    def get_weather(self, city) -> WeatherData:
        pass


# Konkretny adapter dla OpenWeatherMap
class OpenWeatherAdapter(WeatherProvider):
    def get_weather(self, city) -> WeatherData:
        # Symulacja API call
        # response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}")
        # data = response.json()

        # Mapowanie external format -> internal model
        external_data = {
            "main": {"temp": 22.5, "humidity": 65},
            "weather": [{"main": "Clear"}]
        }

        return WeatherData(
            temperature=external_data["main"]["temp"],
            humidity=external_data["main"]["humidity"],
            condition=external_data["weather"][0]["main"]
        )


# Nowe źródło danych - zero zmian w ReportGenerator
class AccuWeatherAdapter(WeatherProvider):
    def get_weather(self, city) -> WeatherData:
        # Inne API, inne format response
        external_data = {
            "current": {"temperature": 23.1, "relative_humidity": 68},
            "conditions": "Sunny"
        }

        # Mapowanie do tego samego internal model
        return WeatherData(
            temperature=external_data["current"]["temperature"],
            humidity=external_data["current"]["relative_humidity"],
            condition=external_data["conditions"]
        )


class ReportGenerator:
    def __init__(self, weather_provider: WeatherProvider):
        # Dependency na stable interface, nie na concrete API
        self.weather_provider = weather_provider

    def generate_weather_report(self, city):
        # Chronione od zmian w external APIs
        weather = self.weather_provider.get_weather(city)

        return f"Weather in {city}: {weather.temperature}°C, {weather.condition}"


class NotificationService:
    def __init__(self, report_generator: ReportGenerator):
        self.report_generator = report_generator

    def send_daily_weather(self, city, user_email):
        # System odporny na zmiany w external APIs
        report = self.report_generator.generate_weather_report(city)
        print(f"Sending to {user_email}: {report}")


if __name__ == "__main__":
    # Łatwo przełączać między providers
    openweather = OpenWeatherAdapter()
    accuweather = AccuWeatherAdapter()

    report_gen1 = ReportGenerator(openweather)
    report_gen2 = ReportGenerator(accuweather)

    service1 = NotificationService(report_gen1)
    service2 = NotificationService(report_gen2)

    service1.send_daily_weather("Warsaw", "user1@example.com")
    service2.send_daily_weather("Krakow", "user2@example.com")

    print("✅ System chroniony przed zmianami w external APIs")
    print("✅ Stable interface pozwala na multiple data sources")
