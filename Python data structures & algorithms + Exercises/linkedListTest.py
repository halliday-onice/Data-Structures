from linkedLists import Node

head = None

#adiciono 5 nos ao inicio da estrutura ligada
for i in range(0,7):
      head = Node(i, head)

while head != None:
      print("->",head.data,end = " ")
      head = head.next

