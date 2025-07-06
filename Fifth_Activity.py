print("hello_world")

def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
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