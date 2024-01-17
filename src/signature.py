from rsa import Key, encryptString

class Signature:
  def __init__(self, message: str, sKey: Key):
    self.message = message
    self.sKey = sKey

def initSignature(message: str, sKey: Key):
  return encryptString(message, sKey)

def writeSignature(sgn: Signature) -> str:
  return '#'.join([str(x) for x in sgn])

def readSignature(str: str) -> Signature:
  return [int(s, 16) for s in str.split('#')]