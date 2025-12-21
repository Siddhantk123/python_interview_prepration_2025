#instancemethod, classmethod, staticmethod
class Area:
    s=10                       # class variabe
    def __init__(self,side):   #instance method, self points to instance of the class
        self.side=side
    
    @classmethod
    def square(cls):        # class point to class
        # print(cls.side)
        print(f"Area of square: {cls.s*cls.s}")
    
    @staticmethod
    def rectangle(len, width):   # works as a normal function without self or cls
        print(f"Area of rectangle: {len*width}")

obj = Area(5)

obj.square()                    #Area of square: 100
Area(5).square()              #Area of square: 100

obj.rectangle(len=2, width=3)     #Area of rectangle: 6
Area(5).rectangle(len=2, width=3) #Area of rectangle: 6