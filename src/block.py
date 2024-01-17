

from hashlib import sha256
from cell import Cell
from protected import Protected, writeProtectedCell
from treeNode import TreeNode
from rsa import Key, writeKey

class Block:
  def __init__(self, author: Key, votes: Cell[Protected]):
    self.author = author
    self.votes = votes
    self.hash = ''
    self.previousHash = ''
    self.nonce = 0

  def initFromBlock(self, author: Key, votes: Cell[Protected], hash: str = '', previousHash: str = '', nonce: int = 0):
    self.author = author
    self.votes = votes
    self.hash = hash
    self.previousHash = previousHash
    self.nonce = nonce

  def write(self):
    return f"{writeKey(self.author)}{self.previousHash}{writeProtectedCell(self.votes)}{hex(self.nonce)[2:]}"

  def updateHash(self):
    self.hash = bin(int(sha256(self.write()).hexdigest(), 16))[2:].zfill(256)

  def verify(self, d: int):
    return self.hash[:d] != '0' * d

  def computeProofOfWork(self, d: int):
    while self.verify(4 * d):
      self.nonce += 1
      self.updateHash()

  def initialize(self, previousBlock = None):
    self.previousHash = previousBlock.hash if previousBlock else ''
    self.computeProofOfWork(2)

  @staticmethod
  def getLongestChain(tree: TreeNode):
    declarations = tree.data.votes
    currentChild = tree.firstChild
    if not currentChild:
      return declarations
    while currentChild.firstChild:
      declarations = Cell.mergeSimple(currentChild.data.votes, declarations)
      currentChild = currentChild.firstChild
    return Cell.mergeSimple(currentChild.data.votes, declarations)