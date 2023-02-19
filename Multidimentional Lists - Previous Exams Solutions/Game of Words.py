# reading the string:
string = input()

# reading the matrix:
rows = int(input())
matrix = []
for row in range(rows):
  matrix.append(list(input()))

# finding the position of the player:
player_position = []
for row in range(rows):
  for column in range(rows):
    if matrix[row][column] == "P":
      player_position = [row, column]

# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1),
}

# reading the commands:
number_of_commands = int(input())
for _ in range(number_of_commands):
  command = input()
  previous_position = player_position.copy()
  if command in directions:
    player_position[0] += directions[command][0]
    player_position[1] += directions[command][1]
    # in the following lines checking if we are outside the field, and if so we retun to our position, and remove the last letter of the string
    if player_position[0] < 0 or player_position[0] == rows:
      player_position[0] -= directions[command][0] 
      if string:
        string = string[:-1]
      continue
    elif player_position[1] < 0 or player_position[1] == rows:
      player_position[1] -= directions[command][1]
      if string:
        string = string[:-1]
      continue
    #now checking if we are stepping on letter or -:
    if matrix[player_position[0]][player_position[1]] not in ["P", "-"]:
      string += matrix[player_position[0]][player_position[1]] # concatinate the current letter to the string
      matrix[player_position[0]][player_position[1]] = "P" # removing the letter that we concatinate from the field, and replacing it with our position P 
      matrix[previous_position[0]][previous_position[1]] = "-" # replacing the previous position with "-"
    else:
      matrix[previous_position[0]][previous_position[1]] = "-"
      matrix[player_position[0]][player_position[1]] = "P"


print(string)

for row in matrix:
  print("".join(row))