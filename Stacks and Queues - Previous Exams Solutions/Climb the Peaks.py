from collections import deque
dictionary = {
  "Vihren": 80,
  "Kutelo": 90,
  "Banski Suhodol": 100,
  "Polezhan": 60,
  "Kamenitza": 70,
}

first_sequence = deque(int(i) for i in input().split(", "))  # pop
second_sequence = deque(int(i) for i in input().split(", ")) # popleft

conquered_peaks = []
day = 1

while dictionary and day <= 7:
  current_energy = first_sequence.pop() + second_sequence.popleft()
  
  for key, value in dictionary.items():
    if current_energy >= value:
      conquered_peaks.append(key)  # adding the conqueued peak
      del dictionary[key]  # deleting the conquered peak from the list
      break
    else:
      break
      
  day += 1


if not dictionary:
  print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
  print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
  print("Conquered peaks:")
  [print(peak) for peak in conquered_peaks]