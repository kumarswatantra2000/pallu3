class Rectangle:

    def set_swatantra(self, height, width):
        self.height = height
        self.width = width
    
    def are(self):

        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
#creating objects
rectangle1 = Rectangle()
rectangle1.set_swatantra(4,3)
print("The height and width area: ", rectangle1.height, rectangle1.width)
print("This is area: ", rectangle1.area())
print("This is perimeter: ", rectangle1.perimeter())