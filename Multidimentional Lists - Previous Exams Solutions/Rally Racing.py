number_of_rows = int(input())
racing_car = input()
# reading the matrix:
matrix = []
for row in range(number_of_rows):
    matrix.append(input().split())
 
distance_covered = 0
car_position = [0, 0]
 
# finding the positions of the tunnels
first_tunnel = []
second_tunnet = []
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == "T":
            if not first_tunnel:
                first_tunnel = [row, column]
            else:
                second_tunnet = [row, column]
                break
 
# creating directions:
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
 
reached_finish_line = False
 
# reading directions:
command = input()
 
while command != "End":
    matrix[car_position[0]][car_position[1]] = "."  # marking the current position as "." before moving
    car_position[0] += directions[command][0]
    car_position[1] += directions[command][1]
 
    if matrix[car_position[0]][car_position[1]] == ".":
        distance_covered += 10
        matrix[car_position[0]][car_position[1]] = "C"
 
    elif matrix[car_position[0]][car_position[1]] == "T":
        distance_covered += 30
        matrix[first_tunnel[0]][first_tunnel[1]] = "."
        matrix[second_tunnet[0]][second_tunnet[1]] = "."
        if car_position[0] == first_tunnel[0] and car_position[1] == first_tunnel[1]:
            car_position[0], car_position[1] = second_tunnet[0], second_tunnet[1]
            matrix[car_position[0]][car_position[1]] = "C"
 
        elif car_position[0] == second_tunnet[0] and car_position[1] == second_tunnet[1]:
            car_position[0], car_position[1] = first_tunnel[0], first_tunnel[1]
            matrix[car_position[0]][car_position[1]] = "C"
 
    elif matrix[car_position[0]][car_position[1]] == "F":
        distance_covered += 10
        reached_finish_line = True
        matrix[car_position[0]][car_position[1]] = "C"
        break
 
    command = input()
 
if reached_finish_line:
    print(f"Racing car {racing_car} finished the stage!")
else:
    matrix[car_position[0]][car_position[1]] = "C"
    print(f"Racing car {racing_car} DNF.")
print(f"Distance covered {distance_covered} km.")
for row in matrix:
    print("".join(row))