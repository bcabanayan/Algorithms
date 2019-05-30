#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    #3 recursive calls
    # n - 1
    # n - 2
    # n - 3
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

def improved_eating_cookies(n, ways):
  # base case, valid way
  if n == 0:
    return 1
  # base case, invalid way
  elif n < 0:
    return 0
  # result found, return without recalculating
  elif n in ways:
    return ways[n]
  # result not found, had to calculate
  else:
    result = improved_eating_cookies(n - 1, ways) + improved_eating_cookies(n - 2, ways) + improved_eating_cookies(n - 3, ways)
    ways[n] = result
    return result

print(improved_eating_cookies(3, {}))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

def improved_eating_cookies(n, ways):
  # base case, valid way
  if n == 0:
    return 1
  # base case, invalid way
  elif n < 0:
    return 0
  # result found, return without recalculating
  elif n in ways:
    return ways[n]
  # result not found, had to calculate
  else:
    result = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    ways[n] = result
    return result
