from calculator import Calculator
from advanced_calculator import AdvancedCalculator
from converter import Converter
from history_manager import HistoryManager
from utils import greet, get_history

def main():
    print(greet("GitHub Learner"))

    # Basic calculator
    calc = Calculator()
    calc.add(10, 5)
    calc.subtract(10, 3)
    calc.multiply(4, 6)
    calc.divide(20, 4)
    calc.divide(10, 0)  # Edge case: division by zero

    print("\n--- Basic Calculation History ---")
    for entry in get_history(calc):
        print(entry)

    # Advanced calculator
    print("\n--- Advanced Calculations ---")
    adv = AdvancedCalculator()
    print("2^10 =", adv.power(2, 10))
    print("sqrt(144) =", adv.square_root(144))
    print("log(1000) =", adv.log(1000))
    print("7! =", adv.factorial(7))
    print("Is 17 prime?", adv.is_prime(17))

    # History manager
    history = HistoryManager()
    for entry in adv.history:
        history.add(entry)
    history.show()
    print("Last entry:", history.last())

    # Converter
    print("\n--- Unit Conversions ---")
    conv = Converter()
    print("100°C in Fahrenheit:", conv.celsius_to_fahrenheit(100))
    print("10 km in miles:", conv.km_to_miles(10))
    print("70 kg in pounds:", conv.kg_to_pounds(70))

if __name__ == "__main__":
    main()
