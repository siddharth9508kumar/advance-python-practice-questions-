<<<<<<< HEAD
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
=======
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
>>>>>>> 4c79a0f634310d5ee974a5ee537d7f8d183c6b03
