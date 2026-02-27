class MaxFinder:
    def __init__(self):
        self.a=list(map(int,input("Enter the numbers: ").split()))
    def find_max(self):
        max_num = self.a[0]
        for num in self.a:
            if num > max_num:
                max_num = num
        return max_num
max_finder = MaxFinder()
print("The maximum number is:", max_finder.find_max())
