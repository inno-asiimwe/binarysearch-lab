class BinarySearch(list):

    def __init__(self, a, b):
        self.extend(list(range(b, a*b+1, b)))
        self.length = a

    def search(self, value):
        count = 0
        found = False
        first = 0
        last = self.length - 1

        while first <= last and not found:
            mid = (first + last)//2

            if self[mid] == value:
                found = True
            elif self[mid] < value:
                first = mid + 1
            else:
                last = mid - 1

        return {'count':count, 'index':mid} if found else {'count':count, 'index':-1}



print(BinarySearch(40, 2).search(33))
