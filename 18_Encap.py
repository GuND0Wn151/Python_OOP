
# We can restrict access to methods and variables. 
# This prevents data from direct modification which is called 
# encapsulation. 


#we denote private attributes using underscore as the prefix i.e single _ or double __.


class Car:
      
    def __init__(self):
        self.__price = 200000

    def sell(self):
        print("Selling Price",self.__price)

    def setMaxPrice(self, price):
        self.__price = price

c = Car()
c.sell()

#changing value using the variable
c.__price = 100000
c.sell()# here as the variabale is private the value doestn change

#chaging the value using a method
c.setMaxPrice(1000)
c.sell()
