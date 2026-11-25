class rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

obj = rectangle(27, 18)
print("Dimension of the rectange is - length", obj.length, "and width", obj.width)
print("Area of the rectangle is:", obj.area())