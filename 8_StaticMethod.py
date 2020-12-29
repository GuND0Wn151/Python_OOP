'''
static methods can be accesed from the class without making object of the class
Therefore a static method can neither modify object state nor class state. 
Static methods are restricted in what data they 
can access - and they’re primarily a way to namespace your methods.
'''
class Student:
      #constructor
      def __init__(self,a,b,c):
            self.name = a
            self.age = b
            self.branch = c
      
      #isntance method
      def PrintAge(self):
           print(self.age)
      
      
      #static methods
      @staticmethod
      def is18Plus(x):
            return x>18
student1 = Student('ram',10,'7th')
student2 = Student('kevin',14,'9th')

"""
static methods are decorated by tag @staticmethod
"""
student1.PrintAge()
student2.PrintAge()

#accesing witht the class name Student
print(Student.is18Plus(17))