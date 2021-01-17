class Car:
      def __init__(self):
            self.wheels=4
            self.color="red"
            self.Enginetype="petrol"


class Benz(Car):  #mentioning the super class here car is the super class of benz
      def __init__(self,model,number,year):
            Car.__init__(self)   #method one for inheritance
            self.model_name=model
            self.car_number=number
            self.manufacturing_year=year
      def displayDetails(self):
            print(self.model_name)
            print(self.car_number)
            print(self.manufacturing_year)
            print(self.wheels)
            print(self.color)
            print(self.Enginetype)
class Tata(Car):
      def __init__(self,model,number,year):
            super().__init__()    #method 2 for inheritance
            self.model_name=model
            self.car_number=number
            self.manufacturing_year=year
      def displayDetails(self):
            print(self.model_name)
            print(self.car_number)
            print(self.manufacturing_year)
            print(self.wheels)
            print(self.color)
            print(self.Enginetype)
c1=Benz("B Class","AUS2313",2021)
c2=Tata("Innova","12312",2020)
c1.displayDetails()
c2.displayDetails()
