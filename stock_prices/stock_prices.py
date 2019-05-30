#!/usr/bin/python

import argparse

def find_max_profit(prices):
  sorted_prices = sorted(prices)
  max_profit_so_far = sorted_prices[0] - sorted_prices[-1]
  for i in range(len(prices)):
    current_min_price_so_far = prices[i]
    for j in range(i + 1, len(prices)):
      profit = prices[j] - current_min_price_so_far
      if profit > max_profit_so_far:
        max_profit_so_far = profit
  return max_profit_so_far

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))