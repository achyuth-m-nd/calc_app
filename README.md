# Python Calculator

A simple Python calculator project — built for practising Git and GitHub workflows.

## Files

| File | Description |
|------|-------------|
| `main.py` | Entry point — runs all demos |
| `calculator.py` | `Calculator` class with add, subtract, multiply, divide |
| `advanced_calculator.py` | Power, square root, log, factorial, prime check |
| `converter.py` | Unit converter for temperature, length, and weight |
| `history_manager.py` | Dedicated history tracking and display |
| `utils.py` | Helper functions (greet, get_history) |
| `test_calculator.py` | Unit tests for basic calculator |
| `test_advanced_calculator.py` | Unit tests for advanced calculator |
| `test_converter.py` | Unit tests for converter |

## How to Run

```bash
# Run the full demo
python main.py

# Run all tests
python -m unittest discover

# Run a specific test file
python -m unittest test_calculator.py
python -m unittest test_advanced_calculator.py
python -m unittest test_converter.py
```

## Concepts Practiced

- Classes and methods
- Error handling (division by zero, invalid inputs)
- Unit testing with `unittest`
- Modular code structure
- Standard library usage (`math` module)
