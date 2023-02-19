# reading the matrix:
matrix = []
for row in range(8):
  matrix.append(input().split())

current_turn = 0  # will be used to know whether we are with white or black pawn, the white is the first one always, so current turn % 2 = 0 means white, otherwise it will be black

white_position = []
black_position = []

white_is_winner = False
white_captured_black = False

black_is_winner = False
black_captured_white = False

# finding the white and black positions:
for row in range(8):
  for column in range(8):
    if matrix[row][column] == "w":
      white_position = [row, column]
    elif matrix[row][column] == "b":
      black_position = [row, column]

# going through the matrix:
while True:
  if current_turn % 2 == 0: # means white position
    new_row = white_position[0] - 1 # going 1 row upwards
    
    # now checking digonaly if there is black:
    if black_position == [new_row, white_position[1] - 1]: # up left
      white_captured_black = True
      break
    elif black_position == [new_row, white_position[1] + 1]: # up right
      white_captured_black = True
      break

    elif new_row == 0:
      white_is_winner = True
      white_position[0] = new_row
      break
      
    else:  # if there is no capture
      current_turn += 1
      white_position[0] = new_row
      

  elif current_turn % 2 != 0 : # meaning black position
    new_row = black_position[0] + 1 # going 1 row downwards
    
    # now checking digonaly if there is white:
    if white_position == [new_row, black_position[1] - 1]: # down left
      black_captured_white = True
      break
    elif white_position == [new_row, black_position[1] + 1]: # down right
      black_captured_white = True
      break
    elif new_row == 7:
      black_is_winner = True
      black_position[0] = new_row
      break  
      
    else:  # if there is no capture
      current_turn += 1
      black_position[0] = new_row


rows= {
  0 : 8,
  1 : 7,
  2 : 6,
  3: 5,
  4: 4,
  5: 3,
  6: 2,
  7: 1,
 
}

colums = {
0: "a",
1: "b",
2:"c",
3: "d",
4: "e",
5: "f",
6: "g",
7: "h" ,
}

if white_is_winner:
  print(f"Game over! White pawn is promoted to a queen at {colums[white_position[1]]}{rows[white_position[0]]}.")

elif black_is_winner:
  print(f"Game over! Black pawn is promoted to a queen at {colums[black_position[1]]}{rows[black_position[0]]}.")

if white_captured_black:
  print(f"Game over! White win, capture on {colums[black_position[1]]}{rows[black_position[0]]}.")

elif black_captured_white:
  print(f"Game over! Black win, capture on {colums[white_position[1]]}{rows[white_position[0]]}.")