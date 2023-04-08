class Rectange():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def f(self): ...
    
class Square(Rectange):
    def __init__(self, a):
        super().__init__(a, a)

    def f(self): print("XD")

x = Square(4)
print(x.area())
x.f()