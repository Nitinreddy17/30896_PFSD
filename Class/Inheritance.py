'''
class parent:
    def function1(self):
        print("this is function one")
class child(parent):
    def function2(self,a):
        print("this is function two")
        print(a)
    b=108

y = child()
y.function1()
y.function2(10)
print(y.b)



from PyCharm.Circlearea import Circle
from PyCharm.AreaSquare import Square
class Result(Circle,Square):
    def res(self):
        print("The Area of Square and Circle is :")

total = Result()
total.res()
total.area(20)
total.area2(10)

'''

class A:
    def __init__(self):
        print("Text Message")
    def sub_method(self, b):
        print("Good",b)

class B(A):
    def __init__(self):
        print("Heist")
        super().__init__()
    def sub_method(self, b):
        print("Day 10",b)
        super().submethod(b + 1)

class C(B):
    def __init__(self):
        print("Init Class C")
        super().

