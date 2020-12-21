class CSGO:
      """
      THis is CSGo class About Attributes
      """
      def __init__(self):
            self.health=100
            self.income=8000
            print("In the Lobby")
      def openInventory(self):
            print("Enter the gun U want to buy")
            self.gun=input()
      def EnterComp(self):
            print("waiting for a match")
      def TakingShots(self):
            print("You have taken shots ur health is reduced")
            print("YOur health is ",self.health-20)



# userdefined attributes

player1=CSGO()
player1.openInventory()
player1.EnterComp()
player1.TakingShots()

#common attributes for a class


'''
apart from normal attributes like entercomp buygun
there are some inbuilt attrivutes whihc can be used for manipulating the object
the most common one are:-
'''


print("getattr= ",getattr(player1,"health")) # output health or 100
print("getattr= ",getattr(player1,"gun")) # output gun which is entered by user
print("hasattr= ",hasattr(player1,"name")) #output False because there is not attribute with name 'name' in class csgo
print("setattr= ",setattr(player1,"health",200)) # changed health from 100 -> 200
print(player1.health) # output 200
print(player1.income) #output = 8000
delattr(player1,"income")  # deletes the attribute income of the object player1
print("hasattr= ",hasattr(player1,"income")) #output =false