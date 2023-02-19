from collections import deque

jobs = [int(i) for i in input().split(", ")]
required_index = int(input())

values_indexes = [(jobs[i], i) for i in range(len(jobs))] # this will return tuples for values and their indexes

deque_values_indexes_sorted = deque(sorted(values_indexes))  # this will sort the tuples based on the values

cycles = 0

while deque_values_indexes_sorted:
  value_index = deque_values_indexes_sorted.popleft()
  current_value = value_index[0]
  current_index = value_index[1]
  cycles += current_value
  if required_index == current_index:
    print(cycles)
    break
    