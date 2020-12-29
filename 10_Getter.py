''''
The getattr() method retu
the value of the named attribute of an object.
If not found, it returns the default value provided to the function.
'''

class person:
      legs=2
      hands=2
      hair_color='black'
      def __init__(self,a):
            self.name=a

person1=person("kevin")

#usual syntax of accesing elements
print(person1.legs)
print(person1.hands)
print(person1.hair_color)


#using getter method
print(getattr(person1,"legs"))
print(getattr(person1,"hands","legs"))

#if used for a unknown attributes throws AttributeError
print(getattr(person1,"age"))