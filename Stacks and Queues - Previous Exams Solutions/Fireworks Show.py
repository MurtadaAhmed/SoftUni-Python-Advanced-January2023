from collections import deque
fireworks = deque(int(i) for i in input().split(", ") if int(i) > 0)  # popleft
explosives = deque(int(i) for i in input().split(", ") if int(i) > 0)  # pop

palm_count = 0
willow_count = 0
crossette_count = 0

while fireworks and explosives:
  if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
    break

  current_firework = fireworks.popleft()
  current_explosive = explosives.pop()
  summed = current_firework + current_explosive

  if summed % 3 == 0 and summed % 5 != 0:
    palm_count += 1

  elif summed % 5 == 0 and summed % 3 != 0:
    willow_count += 1

  elif summed % 3 == 0 and summed % 5 == 0:
    crossette_count += 1

  else:
    current_firework -= 1
    if current_firework > 0:
      fireworks.append(current_firework)
    explosives.append(current_explosive)


successfuly_prepared = palm_count >= 3 and willow_count >= 3 and willow_count >= 3

if successfuly_prepared:
  print("Congrats! You made the perfect firework show!")
else:
  print("Sorry. You can't make the perfect firework show.")

if fireworks:
  print(f"Firework Effects left: {', '.join(str(i) for i in fireworks)}")

if explosives:
  print(f"Explosive Power left: {', '.join(str(i) for i in explosives)}")

print(f"""Palm Fireworks: {palm_count}
Willow Fireworks: {willow_count}
Crossette Fireworks: {crossette_count}""")