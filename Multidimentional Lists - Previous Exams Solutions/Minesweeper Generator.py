number_of_rows = int(input())
# creating the initial matrix with zeros:
matrix = []
for row in range(number_of_rows):
  matrix.append([])
  for column in range(number_of_rows):
    matrix[row].append(0)

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

# reading the number and the positions of the bombs, and placing them in the matrix:
number_of_bumbs = int(input())
for _ in range(number_of_bumbs):
  row, column = eval(input())
  matrix[row][column] = "*"

# going through the matrix, and counting the numbers:
for row in range(number_of_rows):
  for column in range(number_of_rows):
    if matrix[row][column] != "*": # if the current position is not "*"
      for direction in directions:
        new_row = row + directions[direction][0]
        new_column = column + directions[direction][1]
        
        if 0 <= new_row < number_of_rows and 0 <= new_column < number_of_rows: # now checking if we are not outside the matrix:
          if matrix[new_row][new_column] == "*":  # if the nearby position is "*"
            matrix[row][column] += 1 # increase the value of the current field

for row in matrix:
  print(*row)
            