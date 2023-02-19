def forecast(*args):
  dictionary = {"Sunny": [], "Cloudy": [], "Rainy": []}
  for items in args:
    city = items[0]
    weather = items[1]
    dictionary[weather].append(city)

  cleared_dictionary = [(key, value) for key, value in dictionary.items() if value != []]

  items_as_list_sorted = []

  for weather, cities in cleared_dictionary:
    sorted_cities = sorted(cities)
    for city in sorted_cities:
      items_as_list_sorted.append(f"{city} - {weather}")
    
  return "\n".join(items_as_list_sorted)