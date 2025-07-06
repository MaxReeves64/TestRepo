print("hello_world")

import math

def median(input):
  input.sort()
  L = len(input)
  M = L // 2
  if L % 2 == 0:

      return (input[M-1] + input[M])/2

  else:

      return input[M]

my_list = [0, 1, 4, 50]

print(median(my_list))