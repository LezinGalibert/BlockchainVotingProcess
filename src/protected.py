from rsa import decryptArray, readKey, writeKey
from signature import readSignature, writeSignature


class Cell:
  def __init__(self, data):
    self.data = data
    self.next = None

class Protected:
  def __init__(self, pKey, message, signature):
    self.pKey = pKey
    self.message = message
    self.signature = signature

def initProtected(pKey, message, signature):
  return Protected(pKey, message, signature)

def verifyProtected(prot):
  return decryptArray(prot.signature, prot.pKey) == prot.message

def write_protected(prot):
  return f"{writeKey(prot.pKey)} {prot.message} {writeSignature(prot.signature)}"

def read_protected(string):
  items = string.split(' ')
  return Protected(readKey(items[0]), items[1], readSignature(items[2]))

def read_protected_cell_list(prot_list):
  return Cell(prot_list)

def write_protected_cell(prot):
  head = prot.head
  s = ''
  while head:
    s += write_protected(head.data)
    head = head.next
  return s

def sanitize_declarations(declarations):
  current_head = declarations.head
  while current_head:
    if not verifyProtected(current_head.data):
      tmp = current_head
      declarations.delete(tmp)
    current_head = current_head.next