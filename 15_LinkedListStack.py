class Node:
      	

	def __init__(self,value):
            self.value=value
            self.next=None
	def push(self):
		a=int(input("Enter the value "))
		if self.value==None:
			self.__int__(a)
		else:
			newnode=Node(a)
			temp=self
			while temp.next!=None:
				temp=temp.next
			temp.next=newnode
	def pop(self):
		if self.value==None:
			print("Empty")
		else:
			temp=self
			pretemp=None
			while temp.next!=None:
				pretemp=temp
				temp=temp.next
			pretemp.next=None
	def display(self):
		temp=self
		l=[]
		if temp.value==None:
			print("Empty")
		else:
			l.append(temp.value)
			while (temp.next!=None):
				temp=temp.next
				l.append(temp.value)
		
		print("|-------|")
		for i in l[::-1]:
			print("|  ",i,"  |")
			print("|-------|")	
if __name__=="__main__":
	op=int(input("Enter Starting value"))
	st=Node(op)
	while True:
		print("Stack Operations")
		print("1.Push")
		print("2.Pop")
		print("3.Display")
		print("4.Exit")
		a=int(input("Enter your option "))
		if a==1:
			st.push()
		elif a==2:
			st.pop()
		elif a==3:
			st.display()
		else:
			break
	print("Ended")