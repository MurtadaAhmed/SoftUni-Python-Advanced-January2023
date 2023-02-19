def flights(*args):
  dictionary = {}
  if args[0] == "Finish":
    return dictionary
  for index in range(0, len(args), 2):
    flight = args[index]
    if flight == "Finish":
      return dictionary
    passengers = args[index + 1]

    if flight not in dictionary:
      dictionary[flight] = 0
    dictionary[flight] += passengers

  return dictionary