#C0d3 n0=16
#made By GuND0Wn151


class Node:

      def __init__(self,x):
            self.value=x
            self.next=None
      def push(self):
            x=int(input("Enter the value "))
            newnode=Node(x)
            if self.value==None:
                  self.value=x
            elif self.next==None:
                  self.next=newnode
            else:
                  temp=self
                  while temp.next!=None:
                        temp=temp.next
                  temp.next=newnode
      def display(self):
            if self.value==None:
                  print("Empty")
            else:
                  l=[]
                  temp=self
                  while(temp.next!=None):
                        l.append(temp.value)
                        temp=temp.next
                  l.append(temp.value)
            print(*l)
      def pop(self):
            if self.value==None:
                  print("Empty")
            else:
                  self.value=self.next.value
                  self.next=self.next.next
      def peek(self):
            if self.value==None:
                  print("Empty")
            else:
                  print("Top value: ",self.value)

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

