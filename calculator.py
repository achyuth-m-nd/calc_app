class Calculator:
    """A simple calculator class with history tracking."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Error (division by zero)")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
