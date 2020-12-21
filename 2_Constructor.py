

"""
Class with a one parameter constructor
initialized with one parameter whihc is a string called name
"""
class Employer1:
      salary=10000
      
      def __init__(self,name):
            print("In The Employer1 Constructor");
            self.name=name
      def Salary(self, parameter_list):
            """
            docstring
            """
            print(salary)
      def Display(self):
            print("Employer1 Details")
            print("Name: ",self.name)
            print("Salary: ",self.salary)

"""
Class with a zero parameter constructor
initialized (just created object)
creating a method or fucntion whihc assigns the variables

"""
class Employer2:
      def __init__(self):
            print("In The Employer2 Constructor")
      def salary(self,a):
            self.salary=a
      def name(self,a):
            self.name=a
      def Display(self):
            print("Employer2 Details")
            print("Name: ",self.name)
            print("Salary: ",self.salary)
"""
when ever object is created the __init__ method 
asscioated with the class is called and object is created
"""
test1=Employer1("Ram")
test2=Employer2()
test1.Display()
print("-----------------------")
test2.name("Rick")
test2.salary(100)
test2.Display()

