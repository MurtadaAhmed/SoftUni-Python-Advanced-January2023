from collections import deque
def list_manipulator(list, *args):
  order = args[0]
  location = args[1]
  list_as_deque = deque(list)
  
  if order == "add":
    numbers = args[2:]
    if location == "beginning":
      list_as_deque.extendleft(reversed(numbers))  # we use reversed her becasue extendleft reverse the order, so reversed will return the original order
    elif location == "end":
      list_as_deque.extend(numbers)

  elif order == "remove":
    there_is_number = len(args) == 3  # if there is a number, this will be true, else it will be false
    if location == "beginning":
      if there_is_number:
        number = args[-1]
        for turns in range(number):
          list_as_deque.popleft()
      else:
        list_as_deque.popleft()
    elif location == "end":
      if there_is_number:
        number = args[-1]
        for turns in range(number):
          list_as_deque.pop()
      else:
        list_as_deque.pop()
    
  return [int(i) for i in list_as_deque]