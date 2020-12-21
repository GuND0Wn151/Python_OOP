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

print(player1.__doc__,"\n")
print(Valorant.__name__,"\n")
print(Valorant.__dict__,"\n")
print(Valorant.__bases__,"\n")
print(player1.__module__)

