from collections import deque

dictionary = {
"rose": [set("rose"), "rose"],
"tulip": [set("tulip"), "tulip"],
"lotus": [set("lotus"), "lotus"],
"daffodil": [set("daffodil"), "daffodil"]  
}

current_word = set()
word_is_found = False
found_word = ""

vowels = deque(input().split())  # popleft
consonants = deque(input().split()) # pop

while not word_is_found and vowels and consonants:
  current_vowel = vowels.popleft()
  current_consonant = consonants.pop()
  for key, value in dictionary.items(): # in this for loop we are checking if the current vowel and consonat are part of any of the flowes, and if so we add them in current_word
    if set(current_vowel).issubset(value[0]):
      current_word.add(current_vowel)
    if set(current_consonant).issubset(value[0]):
      current_word.add(current_consonant)
      
    for key, value in dictionary.items():  # in this for loop we are checking if any of the flowes are found in current_word
      if value[0].issubset(current_word):
        word_is_found = True
        found_word = value[1]
    
if word_is_found:
  print(f"Word found: {found_word}")
else:
  print("Cannot find any word!")

if vowels:
  print(f"Vowels left: {' '.join(vowels)}")
if consonants:
  print(f"Consonants left: {' '.join(consonants)}")
