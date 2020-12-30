
#C0d3 n0=12
#made By GuND0Wn151
"""
hasattr checks whether a given attribute is there in a object or not
the return value of this fucntion is boolean
=

"""
class Employe:
      name=''
      designation=''
      salary=0

      def __init__(self,a,b,c):
            self.name=a
            self.designation=b
            self.salary=c
      def displayDetails(self):
            print(self.name)
            print(self.designation)
            print(self.salary)


employe1=Employe("Steve","Manager",80000)
employe1.displayDetails()

print(hasattr(employe1,"salary"))
print(getattr(employe1,"designation"))
print(hasattr(employe1,"age"))


