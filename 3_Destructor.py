#C0d3 n0=3
#made By GuND0Wn151

class Car:
      petrol=20
      def __init__(self):
            print("Manufracturing a Car")
      
      def AddPetol(self,x):
            print("petrol added",x)
      def Details(self):
                  print("NO of Wheels to this object is 4")
                  print("This car has ",petrol,"l")
      def __del__(self):
            print("Car is deleted")

class Bike:
      petrol=5
      def __init__(self):
            print("Manufracturing a bike")
      
      def AddPetol(self,x):
            print("petrol added",x)
      def Details(self):
                  print("NO of Wheels to this object is 4")
                  print("This car has ",petrol,"l")
      def __del__(self):     #decleration of dele method
            print("Bike is deleted")


bike1=Bike()
car1=Car()
bike1.AddPetol(10)
car1.AddPetol(20)
del car1 #this deletes the car object
"""
we can make a delete fucntion as __del__
but by default after the exceution of all loc the objects will be deleted like in the bike1 object

"""