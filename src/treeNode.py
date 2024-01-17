class TreeNode:
  def __init__(self, data):
    self.data = data
    self.father = None
    self.firstChild = None
    self.nextBrother = None
    self.height = 0

  def updateHeight(self, child):
    h = self.height
    self.height = max(h, child.height + 1)
    return h == self.height

  def addChild(self, child):
    currentChild = self.firstChild
    child.father = self
    if not currentChild:
      self.firstChild = child
    else:
      while currentChild.nextBrother:
        currentChild = currentChild.nextBrother
      currentChild.nextBrother = child

    newChild = child
    while newChild.father:
      newChild.father.updateHeight(newChild)
      newChild = newChild.father

  def highestChild(self):
    currentChild = self.firstChild
    max_height = 0
    maxHeightChild = currentChild
    while currentChild:
      if max_height < currentChild.height:
        max_height = currentChild.height
        maxHeightChild = currentChild
      currentChild = currentChild.nextBrother
    return maxHeightChild

  def lastNode(self):
    currentChild = self.firstChild
    while currentChild and currentChild.firstChild:
      currentChild = currentChild.highestChild()
    return currentChild

  @staticmethod
  def removeChild(child):
    father = child.father
    if father:
      currentChild = father.firstChild
      if currentChild == child:
        father.firstChild = child.nextBrother
        if father.firstChild:
          father.updateHeight(father.firstChild)
        else:
          father.height = 0
      else:
        while currentChild and currentChild.nextBrother != child:
          currentChild = currentChild.nextBrother
        currentChild = child.nextBrother
      child.father = None
      child.nextBrother = None
      child.height = 0