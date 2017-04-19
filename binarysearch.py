class BinarySearch(list):

    def __init__(self, a, b):
        self.extend(list(range(b, a*b+1, b)))
        self.length = a


print(BinarySearch(20, 1))
