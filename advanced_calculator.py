import math

class AdvancedCalculator:
    """Extends basic calculator with scientific operations."""

    def __init__(self):
        self.history = []

    def power(self, base, exp):
        result = base ** exp
        self.history.append(f"{base} ^ {exp} = {result}")
        return result

    def square_root(self, n):
        if n < 0:
            self.history.append(f"sqrt({n}) = Error (negative number)")
            return None
        result = math.sqrt(n)
        self.history.append(f"sqrt({n}) = {result}")
        return result

    def log(self, n, base=10):
        if n <= 0:
            self.history.append(f"log({n}) = Error (non-positive number)")
            return None
        result = math.log(n, base)
        self.history.append(f"log base {base} of {n} = {result:.4f}")
        return result

    def factorial(self, n):
        if n < 0 or not isinstance(n, int):
            self.history.append(f"{n}! = Error (must be non-negative integer)")
            return None
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
