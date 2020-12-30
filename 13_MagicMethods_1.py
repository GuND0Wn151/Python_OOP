#C0d3 n0=13
#made By GuND0Wn151
"""
there are some methods in python class
      Magic methods in Python are the special methods which add "magic" 
      to your class. Magic methods are not
      meant to be invoked directly by you, but the invocation happens
      internally from the class on a certain action. 
"""


"""
The below is example of overloading the arthematic methods like addition subtraction etc
whihc also returns a object of that class
"""
class Point:
      x=0
      y=0
      
      def __init__(self,a,b):
            self.x=a
            self.y=b
      def __add__(self,a):
            return Point(self.x+a.x ,self.y+a.y)
      def __sub__(self,a):
            return Point(self.x-a.x ,self.y-a.y)
      def __mul__(self,a):
            return Point(self.x*a.x ,self.y*a.y)
      def __floordiv__(self,a):
            return Point(self.x/a.x ,self.y/a.y)


      def displayDetails(self):
            print("X:",self.x,', Y:',self.y)

a=Point(2,3)
b=Point(4,6)
# here + will invoke the overloaded __add__ method in the class and return a object of type Point
f=a+b

# here - will invoke the overloaded __sub__ method in the class and return a object of type Point
g=a-b

# here * will invoke the overloaded __mul__ method in the class and return a object of type Point
h=a*b

# here // will invoke the overloaded __floordiv__ method in the class and return a object of type Point
i=a//b

"""
the return type of the overloaded arthematic options are Point 
so we acces them with the method displayDetails
"""
print(type(f))
f.displayDetails()
print(type(g))
g.displayDetails()
print(type(h))
h.displayDetails()
print(type(i))
i.displayDetails()
