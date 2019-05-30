#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # sort prices to find difference between highest and lowest price
  sorted_prices = sorted(prices)
  max_profit_so_far = sorted_prices[0] - sorted_prices[-1]
  # find buy price 
  for i in range(len(prices)):
    current_min_price_so_far = prices[i]
    # find max profit by looping through each sell price in the array and subtract buy price from the sell price
    for j in range(i + 1, len(prices)):
      profit = prices[j] - current_min_price_so_far
      # if profit is greater than current max profit, then update max profit value
      if profit > max_profit_so_far:
        max_profit_so_far = profit
  return max_profit_so_far

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))