from rsa import Key

class HashCell:
  def __init__(self, key: Key):
    self.key = key
    self.val = 0