class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area_rectangle(self):
        return self.a * self.b

rect_1 = Rectangle(3,4)

print (rect_1.get_area_rectangle())