"""
self has the address of the object whihc we are making 
when print self we get a output like
__main__.object(or)classname at (adress in hex decimal)
"""


class Computer:
      """
      when ever we make a method we have to provide self as a paramter
      whihc assings the values to self
      """
      def __init__(self):
            print("IN Init")
      def processor(self,model):
            self.name=model
      def ramSize(self,ram):
            self.ram=ram
      def display(self):
            print("The processor is",self.name)
            print("the ram size is ",self.ram)
      """
      method whihc prints the self adress
      """
      def whatIsSelf(self):
            print(self)
"""
when we are calling a method like
pc1.display()
the pc1 is taken as a object so 
in this case self = pc1 
and pc1 is a object of class COmputer 
so we get output at <__main__.Computer object at randomadress_in_hex>
"""

pc1=Computer()
pc1.processor("I5")
pc1.ramSize(16)
pc1.display()
pc1.whatIsSelf()