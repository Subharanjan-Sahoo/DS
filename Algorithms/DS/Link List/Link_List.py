'''
ADD/INSERTION:
--------------
-> begin
-> end
-> indetween

   |100|NULL|  -------->NODE

   1010        1074         1120       1134  
 |10|1074|   |20|1120|   |30|1134|   |40|NULL|

  Head                                 
  1010                                
                                         (1) Crate Node
                                         (2) Link List class



'''

class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None 
class LinkedList:
  def __init__(self):
    self.head = None
  def Print_LL(self):
    if self.head is None:
      print("Link List is empty!!")
    else:
      n = self.head
      while n is not None:
        print (n.data)
        n = n.ref

LL1= LinkedList()
LL1.Print_LL()             