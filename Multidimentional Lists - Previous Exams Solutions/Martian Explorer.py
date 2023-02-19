# reading the matrix:
matrix = []
for row in range(6):
  matrix.append(input().split())

# finding the position of the rover:
  rover_position = []
for row in range(6):
  for column in range(6):
    if matrix[row][column] == "E":
      rover_position = [row, column]

# creating directions:
directions = {
  "up": (-1, 0),
  "down": (1, 0),
  "right": (0, 1),
  "left": (0, -1)
}

# reading the movements:
movements = input().split(", ")

water_is_found = False
metal_is_found = False
concrete_is_found = False

for movement in movements:
  rover_position[0] += directions[movement][0]
  rover_position[1] += directions[movement][1]
  # checking if the rover moved outside the matrix:
  if rover_position[0] > 5:
    rover_position[0] = 0
  elif rover_position[0] < 0:
    rover_position[0] = 5
  if rover_position[1] > 5:
    rover_position[1] = 0
  elif rover_position[1] < 0:
    rover_position[1] = 5

  if matrix[rover_position[0]][rover_position[1]] == "W":
    water_is_found = True
    print(f"Water deposit found at ({rover_position[0]}, {rover_position[1]})")
  elif matrix[rover_position[0]][rover_position[1]] == "M":
    metal_is_found = True
    print(f"Metal deposit found at ({rover_position[0]}, {rover_position[1]})")
  elif matrix[rover_position[0]][rover_position[1]] == "C":
    concrete_is_found = True
    print(f"Concrete deposit found at ({rover_position[0]}, {rover_position[1]})")
  elif matrix[rover_position[0]][rover_position[1]] == "R":
    print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
    break

if water_is_found and metal_is_found and concrete_is_found:
  print("Area suitable to start the colony.")
else:
  print("Area not suitable to start the colony.")