# reading players:
first_player, second_player = input().split(", ")
players_hit_wall_counter = {}
players_hit_wall_counter[first_player] = 0
players_hit_wall_counter[second_player] = 0
counter = 0

# reading the matrix:
matrix = []
for row in range(6):
  matrix.append(input().split())

#reading the positions:
while True:
  row, column = eval(input())
  if counter % 2 == 0:
    current_player = first_player
    other_player = second_player
    if players_hit_wall_counter[current_player] == 1:
      players_hit_wall_counter[current_player] = 0
      counter += 1
      continue
      
      
  else:  # counter % 2 != 0
    current_player = second_player
    other_player = first_player
    if players_hit_wall_counter[current_player] == 1:
      players_hit_wall_counter[current_player] = 0
      counter += 1
      continue

  if matrix[row][column] == "E":
    print(f"{current_player} found the Exit and wins the game!" )
    break

  elif matrix[row][column] == "T":
    print(f"{current_player} is out of the game! The winner is {other_player}.")
    break

  elif matrix[row][column] == "W":
    print(f"{current_player} hits a wall and needs to rest.")
    if current_player not in players_hit_wall_counter:
      players_hit_wall_counter[current_player] = 0
    players_hit_wall_counter[current_player] = 1
    
  
  counter += 1
  
  