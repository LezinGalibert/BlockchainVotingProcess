from utils.hashCell import HashCell
from utils.rsa import writeKey


class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [None] * size

  def hashFunction(self, key):
    return (key.modulus + key.exponent) ** 2 % self.size

  def findPosition(self, key):
    keyStr = writeKey(key)
    position = next((i for i, hashCell in enumerate(self.table) if hashCell and writeKey(hashCell.key) == keyStr), -1)
    safetyCount = 0

    if position == -1:
      hashVal = self.hashFunction(key)
      while self.table[hashVal] and writeKey(self.table[hashVal].key) != keyStr and safetyCount < self.size:
        hashVal += 1
        safetyCount += 1
        hashVal %= self.size
      if safetyCount == self.size:
        return None
      position = hashVal
    return position

  def getHashCellForKey(self, key):
    idx = self.findPosition(key)
    return self.table[idx] if idx is not None else None

  def updateCellForKey(self, key):
    cell = self.getHashCellForKey(key)
    if cell:
      cell.val += 1

  def findMax(self):
    currMax = 0
    idx = 0

    for i, cell in enumerate(self.table):
      if cell.val > currMax:
        currMax = cell.val
        idx = i

    return str(currMax), writeKey(self.table[idx].key)

  def initHashTable(self, keys):
    head = keys.head
    while head:
      position = self.findPosition(head.data)
      if position is None:
        break
      hashCell = HashCell(head.data)
      self.table[position] = hashCell
      head = head.next