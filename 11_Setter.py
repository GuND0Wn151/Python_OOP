#C0d3 n0=11
#made By GuND0Wn151

'''
setattr take a object and a variable and value
its assings the varible of the object with the given value
'''
class person:
      legs=2
      hands=2
      hair_color='black'
      age=0
      def __init__(self,a):
            self.name=a



person1=person("kevin")

#usual method of accesing and changin values
person1.age=10
print(person1.age)
print(person1.hair_color)

#using setattr for setting values for age and hair_color
setattr(person1,"age",11)
setattr(person1,"hair_color","white")
print(person1.age)
print(person1.hair_color)
