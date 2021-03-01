class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = str(x)
        self.y = str(y)
        self.width = str(width)
        self.height = str(height)
    def get_rectangle(self):
        return ("Rectangle ("+self.x+", "+self.y+", "+self.width+", "+self.height+")")

rect_1 = Rectangle(5, 10, 50, 100)

print (rect_1.get_rectangle())
print (type (rect_1.get_rectangle()))
