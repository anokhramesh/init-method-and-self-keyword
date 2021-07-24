# Example2 of init and self in python

class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width=width

rect1 = Rectangle(20,60)
rect2 = Rectangle(50,40)
print("Area of rect1 is=",rect1.height*rect1.width)
print("Area of rect2 is=",rect2.height*rect2.width)