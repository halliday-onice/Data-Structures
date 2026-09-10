class Node(object):
      """"Representa um no individualmente ligado"""

      def __init__(self, data, next = None):
            self.data = data
            self.next = next

node1 = None
#node2 conte A em data e nao tem ligacao
node2 = Node("A", None) # quando instanciamos a classe por ex
# node2 . Se eu colocasse node2 = Node("A", node1) node
node3 = Node("B",node2) #


print(node1)
print(node2.data)
print(node3.data)

# se eu quiser fazer com que no 1 ja contenha node2 e node3