def naughty_or_nice_list(list, *args, **kwargs):
  nice_list = []
  naughty_list = []
  not_found = []


  for number_category in args:
    split = number_category.split("-")
    args_number = int(split[0])
    args_category = split[1]
    temporal_list = []
    for list_number, list_name in list:
      if args_number == list_number:
        temporal_list.append(list_name)
        temporal_list.append(list_number)
        temporal_list.append(args_category)

    if len(temporal_list) == 3:  # it means just one name with number and category
      name = temporal_list[0]
      number = temporal_list[1]
      category = temporal_list[2]

      list.remove((number, name))

      if category == "Nice":
        nice_list.append(name)

      elif category == "Naughty":
        naughty_list.append(name)


# the part for args is complete
# now we proceed with kwargs
  


  
  for kwargs_name, kwargs_category in kwargs.items():
    temporal_list = []
    for list_number, list_name in list:
      if kwargs_name == list_name:
        temporal_list.append(list_name)
        temporal_list.append(list_number)
        temporal_list.append(kwargs_category)
        
    if len(temporal_list) == 3:  # it means just one name with number and category
      name = temporal_list[0]
      number = temporal_list[1]
      category = temporal_list[2]

      list.remove((number, name))

      if category == "Nice":
        nice_list.append(name)

      elif category == "Naughty":
        naughty_list.append(name)

  if list: # if there are items left (not found):
    for items in list:
      not_found.append(items[1])

  result = ""
  if nice_list:
    result += f"Nice: {', '.join(nice_list)}\n"
  if naughty_list:
    result += f"Naughty: {', '.join(naughty_list)}\n"
  if not_found:
    result += f"Not found: {', '.join(not_found)}\n"

  return result