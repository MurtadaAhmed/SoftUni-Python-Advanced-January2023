def start_spring(**kwargs):
  dictionary = {}

  for name, type in kwargs.items():
    if type not in dictionary:
      dictionary[type] = []
    dictionary[type].append(name)

  dictionary_sorted = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))

  list_sorted = []

  for type, flowers in dictionary_sorted:
    list_sorted.append(f"{type}:")
    for flower in sorted(flowers):
      list_sorted.append(f"-{flower}")


  return "\n".join(list_sorted)