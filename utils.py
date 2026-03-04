def greet(name):
    """Return a greeting message."""
    return f"Welcome, {name}! Let's do some calculations.\n"

def get_history(calculator):
    """Return the calculation history from a Calculator instance."""
    if not calculator.history:
        return ["No calculations performed yet."]
    return calculator.history
