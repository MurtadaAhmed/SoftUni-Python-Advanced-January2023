def stock_availability(list, command, *args):
  
  if command == "delivery":
    list.extend(args)

  elif command == "sell":
    if not args:
      list.pop(0)
    elif str(args[0]).isdigit():
      number_of_sales = args[0]
      for sale in range(number_of_sales):
        list.pop(0)
    else:
      for item in args:
        while item in list:
          list.remove(item)

  return list