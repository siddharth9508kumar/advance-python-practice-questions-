<<<<<<< HEAD
class SeriesCal:
    def __init__(self, series):
        self.series = series

    def calculate(self):
        return sum(self.series) / len(self.series) if self.series else 0
series_calculator = SeriesCal([1, 2, 3, 4, 5])
result = series_calculator.calculate()
=======
class SeriesCal:
    def __init__(self, series):
        self.series = series

    def calculate(self):
        return sum(self.series) / len(self.series) if self.series else 0
series_calculator = SeriesCal([1, 2, 3, 4, 5])
result = series_calculator.calculate()
>>>>>>> 4c79a0f634310d5ee974a5ee537d7f8d183c6b03
print(f"Result: {result}") 