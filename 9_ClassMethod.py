'''
A class method is a method that
is bound to a class rather than its object.
It doesn't require creation of a class instance, much like staticmethod.
'''
class Student:
      #constructor
      age=0
      def __init__(self,a,b,c):
            self.name = a
            self.age = b
            self.branch = c
      
      #isntance method
      def PrintAge(self):
           print(self.age)
      
      '''
      The difference between a static method and a class method is:
      -- > Static method knows nothing about the class and just deals with the parameters
      -- > Class method works with the class since its parameter is always the class itself.
      '''

      @classmethod
      def ClassMethod(cls,name):
            print(name)
student1 = Student('ram',10,'7th')
student2 = Student('kevin',14,'9th')


student1.PrintAge()
student2.PrintAge()


Student.ClassMethod("hello")