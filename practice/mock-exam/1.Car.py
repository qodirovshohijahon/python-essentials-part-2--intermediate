class Car:
    def __init__(self, x, y):
        self.name = x
        self.price = y

obj1 = Car('Audi', 2000)
obj2 = Car('Audi', 2000)

print(obj1 == obj2)