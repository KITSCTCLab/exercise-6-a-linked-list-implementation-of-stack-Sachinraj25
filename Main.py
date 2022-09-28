class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    if not self.head:
      self.head = Node(data)
    else:
      node = Node(data)
      node.next = self.head
      self.head = node

  def pop(self) -> None:
    if not self.head:
      return 
    else:
      temp = self.head
      self.head = self.head.next
      return temp
    
  def status(self):
    """
    It prints all the elements of stack.
    """
    temp = self.head
    while temp :
      (temp.data,end = "=>")
      temp = temp.next
     print(temp)


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
