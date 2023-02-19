# reading the matrix:
matrix = []
for row in range(8):
  matrix.append(input().split())

# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1),
  "up_right" : (-1, 1),
  "up_left" : (-1, -1),
  "down_right": (1, 1),
  "down_left": (1, -1)
}

queens_positions = []


for row in range(8):
  for column in range(8):
    if matrix[row][column] == "Q":
      for direction in directions:
        current_row = row + directions[direction][0]
        current_column = column + directions[direction][1]
        
        while 0 <= current_row < 8 and 0 <= current_column < 8:  # checking if we are within matrix
          if matrix[current_row][current_column] == "Q":
            break  # breaking the current for loop if we find another Q
          if matrix[current_row][current_column] == "K":
            queens_positions.append([row, column])  # saving the original position of the queen that capture the K
            break
          current_row += directions[direction][0]
          current_column += directions[direction][1]

if queens_positions:
  for row in queens_positions:
    print(row)
else:
  print("The king is safe!")