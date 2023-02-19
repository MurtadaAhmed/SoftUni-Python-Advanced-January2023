def words_sorting(*args):
  dictionary = {}
  sum_of_all_values = 0
  for word in args:
    sum_ascii = 0
    for letter in word:
      sum_ascii += ord(letter)
    dictionary[word] = sum_ascii
    sum_of_all_values += sum_ascii

  if sum_of_all_values % 2 == 0:
    sorted_dictionary = sorted(dictionary.items())
  else:
    sorted_dictionary = sorted(dictionary.items(), key = lambda x: -x[1])

  list_sorted = []
  
  for key, value in sorted_dictionary:
    list_sorted.append(f"{key} - {value}")

  return "\n".join(list_sorted)