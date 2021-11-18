class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

from node import Node

head = None

for count in range(5,0,-1):
    head = Node(count,head)

pro = head
while head != None:
    print(head.data)
    head = head.next