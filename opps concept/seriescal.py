class SeriesCal:
    def __init__(self, series):
        self.series = series

    def calculate(self):
        return sum(self.series) / len(self.series) if self.series else 0
series_calculator = SeriesCal([1, 2, 3, 4, 5])
result = series_calculator.calculate()
print(f"Result: {result}") 