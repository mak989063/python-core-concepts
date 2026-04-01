class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if start < e and end > s:
                return False

        self.events.append([start, end])
        return True

# Create object
cal = MyCalendar()

# Test calls
print(cal.book(10, 20))  # True
print(cal.book(20, 25))  # False
print(cal.book(25, 30))  # True
print(cal.book(15, 25))
print(cal.events)