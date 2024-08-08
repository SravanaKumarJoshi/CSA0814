import math
def is_strong_number(n):
  return n== sum(math.factorial(int(digit))for digit in str(n))
  n=145
  print(is_strong_number(n))
