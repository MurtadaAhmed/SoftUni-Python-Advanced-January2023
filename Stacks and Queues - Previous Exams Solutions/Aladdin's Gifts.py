from collections import deque
materials = deque(int(i) for i in input().split())  # pop
magic = deque(int(i) for i in input().split())  # popleft

gifts_made = {}

gemstone_is_made = False
sculpture_is_made = False
gold_is_made = False
jewellery_is_made = False

while materials and magic:
  current_material = materials.pop()
  current_magic = magic.popleft()
  summed_amount = current_material + current_magic
  if 100 <= summed_amount <= 199:
    gemstone_is_made = True
    if "Gemstone" not in gifts_made:
      gifts_made["Gemstone"] = 0
    gifts_made["Gemstone"] += 1
  elif 200 <= summed_amount <= 299:
    sculpture_is_made = True
    if "Porcelain Sculpture" not in gifts_made:
      gifts_made["Porcelain Sculpture"] = 0
    gifts_made["Porcelain Sculpture"] += 1
  elif 300 <= summed_amount <= 399:
    gold_is_made = True
    if "Gold" not in gifts_made:
      gifts_made["Gold"] = 0
    gifts_made["Gold"] += 1
  elif 400 <= summed_amount <= 499:
    jewellery_is_made = True
    if "Diamond Jewellery" not in gifts_made:
      gifts_made["Diamond Jewellery"] = 0
    gifts_made["Diamond Jewellery"] += 1
  else:
    if summed_amount < 100:
      if summed_amount % 2 ==0:
        current_material *= 2
        current_magic *= 3
        summed_amount = current_material + current_magic
      else:
        summed_amount *= 2

      if 100 <= summed_amount <= 199:
        gemstone_is_made = True
        if "Gemstone" not in gifts_made:
          gifts_made["Gemstone"] = 0
        gifts_made["Gemstone"] += 1
      elif 200 <= summed_amount <= 299:
        sculpture_is_made = True
        if "Porcelain Sculpture" not in gifts_made:
          gifts_made["Porcelain Sculpture"] = 0
        gifts_made["Porcelain Sculpture"] += 1
      elif 300 <= summed_amount <= 399:
        gold_is_made = True
        if "Gold" not in gifts_made:
          gifts_made["Gold"] = 0
        gifts_made["Gold"] += 1
      elif 400 <= summed_amount <= 499:
        jewellery_is_made = True
        if "Diamond Jewellery" not in gifts_made:
          gifts_made["Diamond Jewellery"] = 0
        gifts_made["Diamond Jewellery"] += 1
      
    elif summed_amount > 499:
      summed_amount /= 2
      if 100 <= summed_amount <= 199:
        gemstone_is_made = True
        if "Gemstone" not in gifts_made:
          gifts_made["Gemstone"] = 0
        gifts_made["Gemstone"] += 1
      elif 200 <= summed_amount <= 299:
        sculpture_is_made = True
        if "Porcelain Sculpture" not in gifts_made:
          gifts_made["Porcelain Sculpture"] = 0
        gifts_made["Porcelain Sculpture"] += 1
      elif 300 <= summed_amount <= 399:
        gold_is_made = True
        if "Gold" not in gifts_made:
          gifts_made["Gold"] = 0
        gifts_made["Gold"] += 1
      elif 400 <= summed_amount <= 499:
        jewellery_is_made = True
        if "Diamond Jewellery" not in gifts_made:
          gifts_made["Diamond Jewellery"] = 0
        gifts_made["Diamond Jewellery"] += 1



if (gemstone_is_made and sculpture_is_made) or (gold_is_made and jewellery_is_made):
  print("The wedding presents are made!")
else:
  print("Aladdin does not have enough wedding presents.")

if materials:
  print(f"Materials left: {', '.join(str(i) for i in materials)}")
if magic:
  print(f"Magic left: {', '.join(str(i) for i in magic)}")

gif_made_sorted = sorted(gifts_made.items(), key=lambda x: x[0])
for gift, amount in gif_made_sorted:
  print(f"{gift}: {amount}")