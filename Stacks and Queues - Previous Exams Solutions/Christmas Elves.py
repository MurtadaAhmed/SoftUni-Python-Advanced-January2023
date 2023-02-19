from collections import deque
elves = deque(int(i) for i in input().split())  # popleft
boxes = deque(int(i) for i in input().split())  # pop

toys = 0
energy = 0

current_turn = 1

while elves and boxes:
  current_elf = elves.popleft()
  
  if current_elf < 5:
    continue
  
  current_box = boxes.pop()
  
  if current_turn % 5 == 0 and current_turn % 3 == 0:
    if current_elf >= current_box * 2:
      current_elf -= current_box * 2
      energy += current_box * 2
      elves.append(current_elf)
    else:
      current_elf *= 2
      boxes.append(current_box)
      elves.append(current_elf)
    
  elif current_turn % 3 == 0:
    if current_elf >= current_box * 2:
      toys += 2
      current_elf -= current_box * 2
      current_elf += 1
      energy += current_box * 2
      elves.append(current_elf)
    else:
      current_elf *= 2
      boxes.append(current_box)
      elves.append(current_elf)
    
  elif current_turn % 5 == 0 and current_elf >= current_box:
    current_elf -= current_box
    energy += current_box
    elves.append(current_elf)

  elif current_elf >= current_box:
    toys += 1
    current_elf -= current_box
    current_elf += 1
    energy += current_box
    elves.append(current_elf)

  else:
    current_elf *= 2
    boxes.append(current_box)
    elves.append(current_elf)

  current_turn += 1

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elves:
  print(f"Elves left: {', '.join(str(elf) for elf in elves)}")
if boxes:
  print(f"Boxes left: {', '.join(str(box) for box in boxes)}")