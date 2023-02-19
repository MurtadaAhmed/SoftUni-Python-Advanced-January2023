# reading the matrix:
matrix = []
for row in range(6):
  matrix.append(input().split())
  
# reading the position:
my_position = list(eval(input()))  # eval is to convert the tuple string from the input into tuple, and then list will convert it into a list


# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1)
}

command = input()
while command != "Stop":
  split_command = command.split(", ")
  order = split_command[0]
  movement = split_command[1]

  if order == "Create":
    value = split_command[2]
    my_position[0] = my_position[0] + directions[movement][0]
    my_position[1] = my_position[1] + directions[movement][1]
    if matrix[my_position[0]][my_position[1]] == ".":
      matrix[my_position[0]][my_position[1]] = value
    

  elif order == "Update":
    value = split_command[2]
    my_position[0] = my_position[0] + directions[movement][0]
    my_position[1] = my_position[1] + directions[movement][1]
    if matrix[my_position[0]][my_position[1]] != ".":
      matrix[my_position[0]][my_position[1]] = value

  elif order == "Delete":
    my_position[0] = my_position[0] + directions[movement][0]
    my_position[1] = my_position[1] + directions[movement][1]
    matrix[my_position[0]][my_position[1]] ="."

  elif order == "Read":
    my_position[0] = my_position[0] + directions[movement][0]
    my_position[1] = my_position[1] + directions[movement][1]
    if matrix[my_position[0]][my_position[1]] != ".":
      print(matrix[my_position[0]][my_position[1]])

  command = input()

# printing the final matrix:
for row in matrix:
  print(*row)