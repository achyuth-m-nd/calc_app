class Converter:
    """Unit converter for temperature, length, and weight."""

    # --- Temperature ---
    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

    def celsius_to_kelvin(self, c):
        return c + 273.15

    # --- Length ---
    def km_to_miles(self, km):
        return km * 0.621371

    def miles_to_km(self, miles):
        return miles / 0.621371

    def meters_to_feet(self, m):
        return m * 3.28084

    # --- Weight ---
    def kg_to_pounds(self, kg):
        return kg * 2.20462

    def pounds_to_kg(self, lbs):
        return lbs / 2.20462
