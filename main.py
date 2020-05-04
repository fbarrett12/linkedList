# Creating a singly linked list

class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SlinkedList:
  def __init__(self):
    self.headval = None
  
  def listprint(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval
  
  # def AtBeginning(self, newdata):
  #   NewNode = Node(newdata)
  
# Update the new nodes next value to existing node
    # NewNode.nextval = self.headval
    # self.headval = NewNode

  def AtEnd(self, newdata):
    NewNode = Node(newdata)
    if self.headval is None:
      self.headval = NewNode
      return 
    laste = self.headval
    while(laste.nextval):
      laste = laste.nextval
      laste.nextval = NewNode

list1 = SlinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link the first node to the second node  
list1.headval.nextval = e2

# Link the second node to the third Node
e2.nextval = e3

# Insert new element at the at the beginning of the list
# list1.AtBeginning("Sun")

# Insert new element at the end of the list
list1.AtEnd("Thu")

# Print all values in the list
list1.listprint()