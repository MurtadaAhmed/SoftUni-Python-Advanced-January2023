# reading the rows, columns:
rows, columns = [int(i) for i in input().split(", ")]

# reading the matrix:
matrix = []
for row in range(rows):
  matrix.append(input().split())

# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1),
}

# finding my position and the total number of items:
total_number_of_decoration = 0
total_number_of_gifts = 0
total_number_of_cookies = 0
my_position = []

for row in range(rows):
  for column in range(columns):
    if matrix[row][column] == "Y":
      my_position = [row, column]
    elif matrix[row][column] == "D":
      total_number_of_decoration += 1
    elif matrix[row][column] == "G":
      total_number_of_gifts += 1
    elif matrix[row][column] == "C":
      total_number_of_cookies += 1

all_items_found = False
      
# creating the counters for the found items:
current_number_of_decoration = 0
current_number_of_gifts = 0
current_number_of_cookies = 0

# reading the commands: 
command = input()
while command != "End":
  split_command = command.split("-")
  direction = split_command[0]
  steps = int(split_command[1])
  
  for step in range(steps):
    previous_position = my_position.copy()
    my_position[0] += directions[direction][0]
    my_position[1] += directions[direction][1]
    # checking if we are outside the matrix:
    if my_position[0] == rows:
      my_position[0] = 0
    elif my_position[0] < 0:
      my_position[0] = rows - 1
    if my_position[1] == columns:
      my_position[1] = 0
    elif my_position[1] <0:
      my_position[1] = columns - 1

    #checking if we have an item in the current position:
    if matrix[my_position[0]][my_position[1]] == "D":
      current_number_of_decoration += 1
    elif matrix[my_position[0]][my_position[1]] == "G":
      current_number_of_gifts += 1
    elif matrix[my_position[0]][my_position[1]] == "C":
      current_number_of_cookies += 1

    # as we successfully moved, we need to mark the current position as Y, and the previous position as X:
    matrix[my_position[0]][my_position[1]] = "Y"
    matrix[previous_position[0]][previous_position[1]] = "x"

    # checking if we collected all the items:
    if total_number_of_decoration == current_number_of_decoration and total_number_of_gifts == current_number_of_gifts and total_number_of_cookies == current_number_of_cookies:
      all_items_found = True
      break
  if all_items_found:
    break
  command = input()

if all_items_found:
  print("Merry Christmas!")

print(f"""You've collected:
- {current_number_of_decoration} Christmas decorations
- {current_number_of_gifts} Gifts
- {current_number_of_cookies} Cookies""")

for row in matrix:
  print(" ".join(row))