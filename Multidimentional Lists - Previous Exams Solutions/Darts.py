# reading the names:
first_player, second_player = input().split(", ")
# reading the matrix:
matrix = []
for row in range(7):
  matrix.append(input().split())

first_player_won = False
second_player_won = False

first_player_sum = 501
second_player_sum = 501

first_player_turns = 0
second_player_turns = 0

current_turn = 0 # will be used to know whether we are with the first or the second player

while True:
  row, column = eval(input())
  if current_turn % 2 == 0:  # first player
    first_player_turns += 1
    if 0 <= row < 7 and 0 <= column < 7:
      if matrix[row][column] == "D":
        sum = (int(matrix[0][column]) + int(matrix[6][column]) + int(matrix[row][0]) + int(matrix[row][6])) * 2
        first_player_sum -= sum
      elif matrix[row][column] == "T":
        sum = (int(matrix[0][column]) + int(matrix[6][column]) + int(matrix[row][0]) + int(matrix[row][6])) * 3
        first_player_sum -= sum
      elif matrix[row][column] == "B":
        first_player_won = True
        break
      else: # if it is a number
         first_player_sum -= int(matrix[row][column])

  else: # second player
    second_player_turns += 1
    if 0 <= row < 7 and 0 <= column < 7:
      if matrix[row][column] == "D":
        sum = (int(matrix[0][column]) + int(matrix[6][column]) + int(matrix[row][0]) + int(matrix[row][6])) * 2
        second_player_sum -= sum
      elif matrix[row][column] == "T":
        sum = (int(matrix[0][column]) + int(matrix[6][column]) + int(matrix[row][0]) + int(matrix[row][6])) * 3
        second_player_sum -= sum
      elif matrix[row][column] == "B":
        second_player_won = True
        break
      else: # if it is a number
        second_player_sum -= int(matrix[row][column])
    
      
  if first_player_sum <= 0:
    first_player_won = True
    break
  if second_player_sum <= 0:
    second_player_won = True
    break
  
  current_turn += 1  

if first_player_won:
  print(f"{first_player} won the game with {first_player_turns} throws!")
elif second_player_turns:
  print(f"{second_player} won the game with {second_player_turns} throws!")