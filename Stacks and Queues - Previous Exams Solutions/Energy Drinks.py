from collections import deque

caffeine = deque(int(i) for i in input().split(", "))  # pop
drinks = deque(int(i) for i in input().split(", ")) # popleft

MAXIMUM_CAFFEINE = 300
total_caffeine = 0

while caffeine and drinks:
  current_caffeine = caffeine.pop()
  current_drink = drinks.popleft()
  current_multiplied = current_caffeine * current_drink
  if current_multiplied + total_caffeine <= MAXIMUM_CAFFEINE:
    total_caffeine += current_multiplied
  else:
    drinks.append(current_drink)
    total_caffeine -= 30
    if total_caffeine < 0:
      total_caffeine = 0


if drinks:
  print(f"Drinks left: {', '.join(str(i) for i in drinks)}")
else:
  print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")