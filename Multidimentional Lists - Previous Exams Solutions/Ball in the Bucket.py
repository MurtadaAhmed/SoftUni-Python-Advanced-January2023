# reading the matrix:
matrix = []
for row in range(6):
  matrix.append(input().split())

total_points = 0

# reading the positions:
for _ in range(3):
  row, column = eval(input())
  if 0 <= row < 6 and 0 <= column < 6: # checking if the indexes are valid:
    if matrix[row][column] == "B":
      matrix[row][column] = 0  # removing the B value as per the task
      for row in range(6):
        total_points += int(matrix[row][column])  # adding all the values of the current column to the total points
        
football = 99 < total_points < 200    
teddy_bear = 199 < total_points < 300    
lego_set =  total_points > 299

if lego_set:
  print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
elif teddy_bear:
  print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif football:
  print(f"Good job! You scored {total_points} points, and you've won Football.")
else: # if we did not reach the target
  points_needed = 100 - total_points  # the amount needed to reach the least one which is Football
  print(f"Sorry! You need {points_needed} points more to win a prize.")
