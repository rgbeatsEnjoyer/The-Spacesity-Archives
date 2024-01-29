class Polygon:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def description(self):
        print("A polygon is a straight sided shape with 3 or more sides")
    
class Triangle(Polygon):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def perimeter(self):
        print(self.a + self.b + self.c)

    def description(self):
        print("A triangle has 3 straight sides connected to eachother")
        super().description()

class Rectangle(Polygon):
    def __init__(self,a,b,c, d):
        super().__init__(a,b,c)
        self.d = d 
    
    def perimeter(self):
        print(self.a + self.b + self.c + self.d)
    
    def area(self):
        print(self.a * self.b)

    def description(self):
        print("A rectangle has 4 straight sides, with 2 pairs of equal lengths parallel to eachother")
        super().description()

t1 = Triangle(3,6,9)
t1.description()
r1 = Rectangle(2,4,2,4)
r1.description()

print(~4)

    


        




    
    

