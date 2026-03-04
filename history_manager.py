class HistoryManager:
    """Manages and displays calculation history."""

    def __init__(self):
        self._records = []

    def add(self, entry):
        self._records.append(entry)

    def show(self):
        if not self._records:
            print("No history yet.")
            return
        print("\n--- History ---")
        for i, record in enumerate(self._records, start=1):
            print(f"  {i}. {record}")

    def clear(self):
        self._records.clear()
        print("History cleared.")

    def last(self):
        if self._records:
            return self._records[-1]
        return None

    def count(self):
        return len(self._records)
