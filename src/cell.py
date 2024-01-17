import json

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def addToHead(self, data):
    self.next = Node(data)


class Cell:
  def __init__(self, data):
    head = Node(data[0]) if data else None
    tmp = head
    for k in data[1:]:
      tmp.addToHead(k)
      tmp = tmp.next
    self.head = head

  def delete(self, node):
    nodeStr = json.dumps(node.__dict__)
    tmp = self.head

    if json.dumps(tmp.__dict__) == nodeStr:
      tmp = tmp.next
      self.head = tmp
    else:
      while tmp.next and json.dumps(tmp.next.__dict__) != nodeStr:
        tmp = tmp.next
      if tmp.next:
        tmp.next = tmp.next.next

  @staticmethod
  def mergeSimple(a, b):
    currentHead = a.head

    if not currentHead:
      return b
    while currentHead.next:
      currentHead = currentHead.next
    currentHead.next = b.head
    return a