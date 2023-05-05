from datetime import datetime


class Project:
    def __init__(self, name, start, priority, estimate, completion):
        self.name = name
        self.start = datetime.strptime(start, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = float(estimate)
        self.completion = int(completion)

    def __str__(self):
        return f"{self.name}, start: {self.start.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:,.2f}, completion: {self.completion}%"
