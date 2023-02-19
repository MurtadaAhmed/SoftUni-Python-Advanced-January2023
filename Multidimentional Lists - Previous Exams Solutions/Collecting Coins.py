rows = int(input())
# read the matrix:
matrix = []
for row in range(rows):
  matrix.append(input().split())

coins = 0
my_path = []

# creating the directions
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1),
}

# finding my position:
my_position = []
for row in range(rows):
  for column in range(rows):
    if matrix[row][column] == "P":
      my_position = [row, column]
      break

# adding the current position to my path as per the task:
my_path.append([my_position[0],my_position[1]])

# reading the commands:
while True:
  command = input()
  if command in directions: # checking if the command is valid
    my_position[0] += directions[command][0]
    my_position[1] += directions[command][1]
    # in the following lines checking if we are outside the matrix
    if my_position[0] < 0: 
      my_position[0] = rows - 1
    elif my_position[0] == rows:
      my_position[0] = 0
    if my_position[1] < 0: 
      my_position[1] = rows - 1
    elif my_position[1] == rows:
      my_position[1] = 0
    # adding our new position to the path:
    my_path.append([my_position[0],my_position[1]])
    
    if matrix[my_position[0]][my_position[1]] == "X": # checking whether we are stepping on number or X
      coins = int(coins * 0.5)
      print(f"Game over! You've collected {coins} coins.")
      break
    elif matrix[my_position[0]][my_position[1]].isdigit():  # checking whether we are stepping on a number
      coins += int(matrix[my_position[0]][my_position[1]])
      matrix[my_position[0]][my_position[1]] = "P" # removing the coins from the current position and replacing it with random thing like "P"
    
  # now we need to check if we have collected 100 coins:
  if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
    break

# in the end we need to print the path:
print("Your path:")  
for row in my_path:
  print(row)