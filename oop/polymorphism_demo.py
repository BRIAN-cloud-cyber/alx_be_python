
import math
class Shape:
        def area(self):
            """Calculate area of shape.
            Must be overriden by subclasses
            """
            raise NotImplementedError("subclasses must implement area()")
class Rectangle(Shape):
        def __init__(self,length,width):
            self.length=length
            self.width=width

        def area(self):
            return self.length*self.width
class Circle(Shape):
        def __init__(self,radius):
            self.radius=radius

        def area(self):
            return math.pi *(self.radius**2)
        
def main():
    Shapes=[Rectangle(4,5),
            Circle(3)]
    for Shape in Shapes:
         print(f"Area:{Shape.area()}")
if __name__=="__main__":
    main()
        
        
