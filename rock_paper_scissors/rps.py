#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = [['rock'],['paper'],['scissors']]
  final_list = [[]]
  if n == 0:
    return final_list

print(rock_paper_scissors(1))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')