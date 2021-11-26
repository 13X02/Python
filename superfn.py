class Quadrilateral:
    def __init__(self,height,width):
        self.height = height
        self.width = width
class Rectangle(Quadrilateral):
    def __init__(self, height, width):
        super().__init__(height, width)
    def area(self):
        return self.height * self.width


a = Rectangle(3,5)
print(a.area())