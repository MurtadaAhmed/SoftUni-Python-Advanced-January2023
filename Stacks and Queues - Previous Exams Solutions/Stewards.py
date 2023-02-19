from collections import deque
seats = input().split(", ")
first_sequence = deque(input().split(", ")) # we take from the left side >> popleft
second_sequence = deque(input().split(", ")) # we take from the right side >> pop

seat_matches = []
rotation_count = 0


while rotation_count < 10 and len(seat_matches) < 3:
  first_number = first_sequence.popleft()
  second_number = second_sequence.pop()
  letter = chr(int(first_number) + int(second_number))
  first_match = first_number + letter
  second_match = second_number + letter
  rotation_count += 1
  if first_match in seat_matches or second_match in seat_matches:  # if matches an already matched seat
    continue
  if first_match in seats:
    seat_matches.append(first_match)
  elif second_match in seats:
    seat_matches.append(second_match)
  else:  # if there is no equality
    first_sequence.append(first_number)
    second_sequence.appendleft(second_number)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotation_count}")