class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)

print(a.first)
print(a.second)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(5, 3)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)

print(a.div())

class Family:
    lastname = "김"

print(Family.lastname)