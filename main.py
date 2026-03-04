from calculator import Calculator
from utils import greet, get_history

def main():
    print(greet("GitHub Learner"))
    calc = Calculator()

    calc.add(10, 5)
    calc.subtract(10, 3)
    calc.multiply(4, 6)
    calc.divide(20, 4)
    calc.divide(10, 0)  # Edge case: division by zero

    print("\n--- Calculation History ---")
    for entry in get_history(calc):
        print(entry)

if __name__ == "__main__":
    main()
