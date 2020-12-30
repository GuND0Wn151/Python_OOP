#C0d3 n0=7
#made By GuND0Wn151
'''
Instance are the attribute or things which a class or object possess has
Every object has its own copy of the instance attribute
'''
class Car:
      # here name is a class attribute
      name=""

      # and also horn noOfWheels are called instance methods
      def __init__(self,x):
            self.name=x # here now name is a instance attribute
            print("in init")
      def horn(self):
            print("Horn")
      def noOfWheels(self):
            print("car has 4 wheels")
'''
To list the attributes of an instance/object, we have two functions:-
1. vars()– This function displays the attribute of an instance in the form of an dictionary.
2. dir()– This function displays more attributes than vars function,as it is not limited to instance.
          It displays the class attributes as well. It also displays the attributes of its ancestor classes.
'''


car1=Car("benz")
car1.horn()
car1.noOfWheels()
print(vars(car1))
print(dir(car1))
