from primeSearch import extendedGCD, modpow, pickRandomNumber, randomPrimeNumberBySize

class Key:
  def __init__(self, exponent, modulus):
    self.exponent = exponent
    self.modulus = modulus

def generateKeyValues(p, q):
  n = p * q
  t = (p - 1) * (q - 1)

  s = pickRandomNumber(0, t)
  while extendedGCD(s, t)['gcd'] != 1:
    s = pickRandomNumber(0, t)
  u = extendedGCD(s, t)['u']
  if u <= 0:
    u += t
  return Key(exponent=s, modulus=n), Key(exponent=u, modulus=n)

def encryptString(string, key):
  encodedArray = []

  for char in string:
    encodedArray.append(modPow(ord(char), key.exponent, key.modulus))
  return encodedArray

def decryptArray(array, key):
  newArray = [modPow(item, key.exponent, key.modulus) for item in array]
  return ''.join([chr(item) for item in newArray])

def initKeyPair(lowerSize, upperSize, k=5000):
  p = randomPrimeNumberBySize(lowerSize, upperSize, k)
  q = randomPrimeNumberBySize(lowerSize, upperSize, k)

  while p == q:
    q = randomPrimeNumberBySize(lowerSize, upperSize, k)

  return generateKeyValues(p, q)

def writeKey(key):
  return f"({hex(key.exponent)}, {hex(key.modulus)})"

def readKey(string):
  res = string.split(',')
  exponent = int(res[0][1:], 16)
  modulus = int(res[1][:-1], 16)
  return Key(exponent=exponent, modulus=modulus)