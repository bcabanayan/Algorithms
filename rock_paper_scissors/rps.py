#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  final_list = []
  options = [['rock'],['paper'],['scissors']]
  # def add_plays(plays_so_far):
  #   for i in plays_so_far:
  #     for j in plays:
  #       i = i + j
  #     return plays_so_far
  if n == 0:
    return [[]]
  else:
    previous_plays = rock_paper_scissors(n - 1)
    for previous_play in previous_plays:
      for option in options:
        final_list.append(previous_play + option)
  return final_list
  
print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')