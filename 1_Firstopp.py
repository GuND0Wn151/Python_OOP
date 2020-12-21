class Car:
      #__init is constructor whihc instantiates an object
      name=""
      def __init__(self,x):
            self.name=x
            print("in init")
      #methods in which can be declared
      def horn(self):
            print("Horn")
      def noOfWheels(self):
            print("car has 4 wheels")

#TO Use The class create a object of that class
#by default the python calls the __init__ function for creating the object
person=Car("Ram")  #this calls the __init__ and the print statement in fucntions run

#TO use a object variable use objectName.variableName
#this does return a value whihc can be stored or printed
print(person.name)

#For calling methods or fucntions of the class use the object
#objectName.FUnctionName
person.horn()
person.noOfWheels()
