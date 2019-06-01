#!/usr/bin/python

import sys

# can kind of follow same set up as eating cookies
# getting from an initial value to zero!

# denominations = [1, 5, 10, 25, 50]

def making_change(amount, denominations, ways):
  if amount == 0:
    return 1
  elif amount < 0:
    return 0
  elif amount in ways:
    return ways[amount]
  else:
    result = 0
    for i in range(len(denominations) - 1, -1, -1):
      result = result + making_change(amount - denominations[i], denominations, ways)
    ways[amount] = result
    if result.sort() not in ways:
      return result

print(making_change(10, [1, 5, 10, 25, 50], {}))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")