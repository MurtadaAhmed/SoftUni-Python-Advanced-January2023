from collections import deque
eggs_size = deque(int(i) for i in input().split(", "))  # popleft
paper_size = deque(int(i) for i in input().split(", "))  # pop
BOX_SIZE = 50
total_boxes = 0
while eggs_size and paper_size:
  current_egg = eggs_size.popleft()
  if current_egg <= 0:
    continue
  elif current_egg == 13:
    paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]  # swapping the first and last papers
  else:
    current_paper = paper_size.pop()
    if current_egg + current_paper <= BOX_SIZE:
      total_boxes += 1

if total_boxes:
  print(f"Great! You filled {total_boxes} boxes.")
else:
  print("Sorry! You couldn't fill any boxes!")

if eggs_size:
  print(f"Eggs left: {', '.join(str(egg) for egg in eggs_size)}")
if paper_size:
  print(f"Pieces of paper left: {', '.join(str(paper) for paper in paper_size)}")
