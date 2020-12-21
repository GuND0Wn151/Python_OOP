#C0d3 n0=6
#made By GuND0Wn151


class Valorant:
      """
      Valorant class this class has attributes as health agent gun
      """
      def __init__(self):
            print("welcome to lobby")
            self.health=100
      def GetReady(self):
            print("Entering the match")
            print("Enteer the the agent u want to pick")
            self.agent=input()
      def BuyGun(self):
            print("Enter the Gun u want to buy")
            self.gun=input()
      def UseUltimate(self):
            print("Ultimate Attack!!!")
      def display(self):
            print(self.agent)
            print(self.gun)
            print(self.health)
      
"""
apart from some attributes like getattr and hasattr there are some usefull builtin attributes
which can be useful during solving problems they are
"""
player1=Valorant()
player1.GetReady()
player1.BuyGun()
player1.display()

#__doc__ gives the docmentation in the class if nthg is meantioned then it returns non
print(player1.__doc__,"\n")

#__name__ return name of the class
print(Valorant.__name__,"\n")

#this attributes returns a dictonary whihc has the all attributes of the class mentioned and also with their address
# and also the adress of variables used in the class
print(Valorant.__dict__,"\n")

# possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print(Valorant.__bases__,"\n")

# Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print(player1.__module__)

#this are the some useful builtin attributes of python classes and objects