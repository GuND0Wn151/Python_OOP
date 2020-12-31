#C0d3 n0=14
#made By GuND0Wn151

class Node:
      def __init__(self,value):
            self.value=value
            self.next=None

      def isEmpty(self):
            if self.value==None:
                  return True
            else:
                  return False

      def LLappend(self):
            x=int(input("Enter date"))

            if self.isEmpty():
                  self.value=x
            elif self.next==None:
                  newnode=Node(x)
                  self.next=newnode
            else:
                  temp=self
                  while(temp.next!=None):
                        temp=temp.next
                  newnode=Node(x)
                  temp.next=newnode

      def LLdisplay(self):
            temp=self
            l=[]
            if temp.value==None:
                  print("Empty")
            else:
                  l.append(temp.value)
                  while (temp.next!=None):
                        temp=temp.next
                        l.append(temp.value)
            print("\n",*l)
            
      def insert(self):
            print("\nEnter the postion: ")
            a=int(input())
            print("\nEnter the value: ")
            x=int(input())
            if(a==1):
                  val=self.value
                  newnode=Node(val)
                  self.value=x
                  temp=self.next
                  self.next=newnode
                  newnode.next=temp

            else:
                  temp=self
                  newnode=Node(x)
                  while (a!=1):
                        a-=1
                        pretemp=temp
                        temp=temp.next
                  pretemp.next=newnode
                  newnode.next=temp

      def delete(self):
            print("\nEnter the value: ")
            x=int(input())
            temp=self
            pretemp=None
            if self.value==x:
                  self.value=None
                  if (self.next!=None):
                        self.value=self.next.value
                        self.next=self.next.next
            else:
                  while (temp.value!=x):
                        pretemp=temp
                        temp=temp.next
                  pretemp.next=temp.next
                        
if __name__=="__main__":
      x=int(input("Enter the starting value of Linked List "))
      ll=Node(x)
      while True:
            print("=========================================================")
            print("=======================Linked List=======================")

            print("""\n1.Insert
            \n2.Append
            \n3.Delete
            \n4.Display
            \n5.Exit""")
            opt=int(input("\nEnter your option "))
            if opt==1:
                  ll.insert()
            elif opt==2:
                  ll.LLappend()
            elif opt==3:
                  ll.delete()
            elif opt==4:
                  ll.LLdisplay()
            else:
                  break
      print("=========================================================")