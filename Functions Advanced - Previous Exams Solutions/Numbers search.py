def numbers_searching(*args):
  list_with_duplicats = []

  for number in args:
    if args.count(number) >= 2:
      if number not in list_with_duplicats:
        list_with_duplicats.append(number)



  # now finding the missing number:
  missing_number = 0
  list_sorted = sorted(args)
  
  for number in range(list_sorted[0], list_sorted[-1] + 1):  # range if from the smallest number to the biggest number in the list
    if number not in list_sorted:
      missing_number = number

  result = [] # because the result has to be a list as per the task
  result.append(missing_number)
  result.append(sorted(list_with_duplicats))
  return result