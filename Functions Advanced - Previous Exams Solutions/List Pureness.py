from collections import deque
def best_list_pureness(*args):
  list = args[0]
  rotations = args[1]
  list_as_queue = deque(list)

  highest_purness = 0
  best_rotation_count = 0

  rotation_count = 0
  
  # checking the purness before we rotate:
  for index, value in enumerate(list_as_queue):
    highest_purness += index * value
  

  # now we check the purness for each rotation
  for _ in range(rotations):
    removed = list_as_queue.pop()
    list_as_queue.appendleft(removed)
    current_pureness = 0
    rotation_count += 1
    for index, value in enumerate(list_as_queue):
      current_pureness += index * value
    if current_pureness > highest_purness:
      highest_purness = current_pureness
      best_rotation_count = rotation_count


  return f"Best pureness {highest_purness} after {best_rotation_count} rotations"