# reading the matrix:
rows = int(input())
matrix = []
for row in range(rows):
  matrix.append(list(input()))

# finding the position of the snake and the two burrows:
snake_position = []
first_burrow = []
second_borrow = []
for row in range(rows):
  for column in range(rows):
    if matrix[row][column] == "S":
      snake_position = [row, column]
    elif matrix[row][column] == "B":
      if not first_burrow:
        first_burrow = [row,column]
      else:
        second_borrow = [row, column]

# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1),
}

food_count = 0

# reading the commands:
while True:
  command = input()
  matrix[snake_position[0]][snake_position[1]] = "."  # replacing the position before the movement with "."
  snake_position[0] += directions[command][0]
  snake_position[1] += directions[command][1]
  if snake_position[0] == rows or snake_position[0] < 0 or snake_position[1] == rows or snake_position[1] < 0: # snake went outside the field
    print("Game over!")
    break
  else: # if we are within the field
    if matrix[snake_position[0]][snake_position[1]] == "*":
      food_count += 1
      matrix[snake_position[0]][snake_position[1]] = "S"  # because the snake moved to this position
      if food_count == 10:
        print("You won! You fed the snake.")
        break
    elif matrix[snake_position[0]][snake_position[1]] == "B":
      if first_burrow == [snake_position[0], snake_position[1]]:
        matrix[snake_position[0]][snake_position[1]] = "."  # marking the current "B" position as "."
        snake_position[0] = second_borrow[0]
        snake_position[1] = second_borrow[1]
        matrix[snake_position[0]][snake_position[1]] = "S" # marking the second "B" position as "S"
      elif second_borrow == [snake_position[0], snake_position[1]]:
        matrix[snake_position[0]][snake_position[1]] = "."
        snake_position[0] = first_burrow[0]
        snake_position[1] = first_burrow[1]
        matrix[snake_position[0]][snake_position[1]] = "S"
    
  
print(f"Food eaten: {food_count}")  
for row in matrix:
  print("".join(row))