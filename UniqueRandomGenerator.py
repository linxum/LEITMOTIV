import random

class UniqueRandomGenerator:
    def __init__(self, start, end):
        self.numbers = list(range(start, end + 1))
        random.shuffle(self.numbers)

    def generate_random_number(self):
        if not self.numbers:
            raise ValueError("No more unique numbers left to generate.")
        return self.numbers.pop()