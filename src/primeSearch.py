import random

def pickRandomNumber(low: int, up: int) -> int:
  return random.randint(low, up)

#Recursively calculates a^m mod n
def modpow(a: int, m: int, n: int) -> int:
  if (m == 0):
    return 1
  elif (m % 2 == 0):
    return (modpow(a, m / 2, n) * modpow(a, m / 2, n)) % n
  else:
    return (a * modpow(a, (m - 1) / 2, n) * modpow(a, (m - 1) / 2, n)) % n

  # Find a witness for Miller Rabin prime test:
# Let p be an odd integer, and b & d two integers such that p = 2b^d + 1. Let a
# such that a < p, a is a witness for Miller's test if:
# - a^d mod p != 1
# - a^(2^r)d mod p != -1 for r < b (integer)
# If a is a Miller's witness for p, then p is not prime.
def millerWitness(a: int, b: int, d: int, p: int) -> bool:
  x = modpow(a, d, p)
  if x == 1:
    return False

  for i in range(b):
    if x == p - 1:
      return False
    else :
      x = modpow(x, 2, p)

  return True

def isMillerPrime(p: int, k: int) -> bool:
  if p == 2:
    return True

  if p % 2 == 0 or p <= 1:
    return False

  b = 0
  d = p - 1

  while d % 2 == 0:
    d //= 2
    b += 1

  a = 0

  for i in range(k):
    a = pickRandomNumber(2, p - 1)
    if millerWitness(a, b, d, p):
      return False

  return True

def randomPrimeNumberBySize(lowSize: int, upSize: int, k: int) -> int:
  potentialPrime = pickRandomNumber(2 ** (lowSize - 1), 2 ** upSize - 1)

  while not isMillerPrime(potentialPrime, k):
    potentialPrime = pickRandomNumber(2 ** (lowSize - 1), 2 ** upSize - 1)

  return potentialPrime

def randomPrimePairBySize(lowSize: int, upSize: int, k: int):
  p = randomPrimeNumberBySize(lowSize, upSize, k)
  q = randomPrimeNumberBySize(lowSize, upSize, k)

  while p == q:
    q = randomPrimeNumberBySize(lowSize, upSize, k)

  return [p, q]

def extendedGCD(s: int, t: int):
  if s == 0:
    return {'gcd': t, 'u': 0, 'v': 1}
  result = extendedGCD(t % s, s)
  gcd = result['gcd']
  u = result['u']
  v = result['v']
  uFinal = v - (t // s) * u
  vFinal = u
  return {'gcd': gcd, 'u': uFinal, 'v': vFinal}