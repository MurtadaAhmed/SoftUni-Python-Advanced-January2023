number_of_rows = int(input())
matrix = [[i for i in list(input())] for _ in range(number_of_rows)]

sumbarine_position = []  # S
hits_taken = 0  # *
cruisers_count = 0  # C

directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1)
}

for row in range(len(matrix)):
  for column in range(len(matrix[row])):
    if matrix[row][column] == "S":
      sumbarine_position = [row, column]  # the position of S
      


while hits_taken < 3 and cruisers_count < 3:
  
  command = input()
  matrix[sumbarine_position[0]][sumbarine_position[1]] = "-" # changing the current position from "S" to "-" when moving in next lines
  sumbarine_position[0] += directions[command][0]
  sumbarine_position[1] += directions[command][1]
  
  if matrix[sumbarine_position[0]][sumbarine_position[1]] == "*":
    hits_taken += 1
    matrix[sumbarine_position[0]][sumbarine_position[1]] = "S"
  elif matrix[sumbarine_position[0]][sumbarine_position[1]] == "C":
    cruisers_count += 1
    matrix[sumbarine_position[0]][sumbarine_position[1]] = "S"
  else:
    matrix[sumbarine_position[0]][sumbarine_position[1]] = "S"
    

if cruisers_count >= 3:
  print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
if hits_taken >= 3:
  print(f"Mission failed, U-9 disappeared! Last known coordinates {sumbarine_position}!")

for row in matrix:
  print("".join(row))