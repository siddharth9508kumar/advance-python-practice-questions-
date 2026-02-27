class Result:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Name: {self.name}, Score: {self.score}")
result1 = Result("Alice", 85)
result1.display()  