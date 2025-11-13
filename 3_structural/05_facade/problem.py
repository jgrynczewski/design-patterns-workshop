"""
❌ PROBLEM: Klient bezpośrednio zarządza wieloma podsystemami

Rozwiązanie bez wzorca Facade:
- Klient musi znać wszystkie klasy podsystemów (Light, Thermostat, Security, TV)
- Klient musi pamiętać sekwencję wywołań dla każdej akcji
- Duplikacja logiki w wielu miejscach kodu klienta
"""


class Light:
    """Podsystem - oświetlenie"""

    def turn_on(self) -> str:
        return "Light turned ON"

    def turn_off(self) -> str:
        return "Light turned OFF"

    def dim(self, level: int) -> str:
        return f"Light dimmed to {level}%"


class Thermostat:
    """Podsystem - termostat"""

    def set_temperature(self, temp: int) -> str:
        return f"Thermostat set to {temp}°C"


class SecuritySystem:
    """Podsystem - alarm"""

    def arm(self) -> str:
        return "Security system ARMED"

    def disarm(self) -> str:
        return "Security system DISARMED"


class TV:
    """Podsystem - telewizor"""

    def turn_on(self) -> str:
        return "TV turned ON"

    def turn_off(self) -> str:
        return "TV turned OFF"


# ❌ Przykład użycia - klient zarządza wszystkim
if __name__ == "__main__":
    # ❌ PROBLEM: Klient musi stworzyć wszystkie podsystemy
    light = Light()
    thermostat = Thermostat()
    security = SecuritySystem()
    tv = TV()

    # ❌ PROBLEM: Klient musi pamiętać sekwencję dla "trybu wieczornego"
    print("=== Evening Mode ===")
    print(light.dim(50))
    print(thermostat.set_temperature(22))
    print(security.disarm())
    print(tv.turn_on())

    # ❌ PROBLEM: Klient musi pamiętać inną sekwencję dla "wychodzenia"
    print("\n=== Leaving Home ===")
    print(light.turn_off())
    print(thermostat.set_temperature(18))
    print(security.arm())
    print(tv.turn_off())

    # ❌ Każde miejsce w kodzie, które potrzebuje "evening mode"
    # musi powtarzać te 4 linie
    #
    # ❌ Zmiana sekwencji wymaga edycji w wielu miejscach
    #
    # ❌ Nowy programista musi znać wszystkie 4 klasy podsystemów


"""
Jakie problemy rozwiązuje Facade?

1. ❌ Zbyt wiele zależności
   - Klient zależy od Light, Thermostat, SecuritySystem, TV
   - Dodanie nowego podsystemu wymaga zmian w kliencie
   - Wysokie sprzężenie (tight coupling)

2. ❌ Duplikacja logiki
   - "Evening mode" może być używany w 10 miejscach
   - Każde miejsce powtarza te same 4 wywołania
   - Zmiana sekwencji = edycja 10 miejsc

3. ❌ Trudne utrzymanie
   - Klient musi znać szczegóły implementacji podsystemów
   - Klient musi pamiętać prawidłową kolejność wywołań
   - Łatwo o błąd (zapomnienie jednego kroku)

4. ❌ Brak abstrakcji
   - Klient operuje na niskim poziomie (dim, set_temperature)
   - Brak operacji wysokiego poziomu (evening_mode, leaving_home)
   - Kod trudny do zrozumienia

5. ❌ Trudne testowanie
   - Testowanie klienta wymaga mockowania 4 klas
   - Każdy test musi setupować wszystkie podsystemy
   - Duża liczba zależności

Jak Facade to rozwiązuje?
1. SmartHomeFacade ukrywa wszystkie podsystemy
2. Klient wywołuje home.evening_mode() zamiast 4 metod
3. Logika sekwencji w jednym miejscu (Facade)
4. Łatwe testowanie - mockujemy tylko Facade
"""
