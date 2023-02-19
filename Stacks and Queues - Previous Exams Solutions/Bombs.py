from collections import deque

effects = deque(int(i) for i in input().split(", "))  # popleft
casings = deque(int(i) for i in input().split(", "))  # pop

datura_count = 0
cherry_count = 0
smoke_decoy_count = 0

while effects and casings:
  if datura_count >= 3 and cherry_count >= 3 and smoke_decoy_count >= 3:
    break
  current_effect = effects.popleft()
  current_casing = casings.pop()

  summed = current_effect + current_casing

  if summed == 40:
    datura_count += 1
  elif summed == 60:
    cherry_count += 1
  elif summed == 120:
    smoke_decoy_count += 1
  else:
    current_casing -= 5
    casings.append(current_casing)
    effects.appendleft(current_effect)

succeded = datura_count >= 3 and cherry_count >= 3 and smoke_decoy_count >= 3

if succeded:
  print("Bene! You have successfully filled the bomb pouch!")
else:
  print("You don't have enough materials to fill the bomb pouch.")

if effects:
  print(f"Bomb Effects: {', '.join(str(i) for i in effects)}")
else:
  print("Bomb Effects: empty")

if casings:
  print(f"Bomb Casings: {'. '.join(str(i) for i in casings)}")
else:
  print("Bomb Casings: empty")

print(f"""Cherry Bombs: {cherry_count}
Datura Bombs: {datura_count}
Smoke Decoy Bombs: {smoke_decoy_count}""")
