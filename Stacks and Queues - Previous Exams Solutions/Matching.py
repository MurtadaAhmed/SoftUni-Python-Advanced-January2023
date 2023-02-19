from collections import deque
males = deque(int(i) for i in input().split() if int(i) > 0)  # pop
females = deque(int(i) for i in input().split() if int(i) > 0)  # popleft

matches_count = 0

while males and females:
  current_male = males.pop()
  current_female = females.popleft()
  
  if current_male % 25 == 0 and current_female % 25 != 0:
    males.pop()
    females.appendleft(current_female)
    continue
  elif current_female % 25 == 0 and current_male % 25 != 0:
    females.popleft()
    males.append(current_male)
    continue
  elif current_male % 25 == 0 and current_female % 25 == 0:
    males.pop()
    females.popleft()
    continue

  
  if current_male != current_female:
    current_male -= 2
    if current_male > 0:
      males.append(current_male)
  else:
    matches_count += 1
  



print(f"Matches: {matches_count}")

if males:
  print(f"Males left: {', '.join(str(i) for i in reversed(males))}")
else:
  print("Males left: none")

if females:
  print(f"Females left: {', '.join(str(i) for i in females)}")
else:
  print("Females left: none")