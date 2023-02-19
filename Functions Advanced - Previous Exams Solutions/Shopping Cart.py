def shopping_cart(*args):
  dictionary = {"Soup": [], "Pizza": [], "Dessert": []}

  for items in args:
    if items == "Stop":
      break
    meal = items[0]
    product = items[1]
    
    if meal == "Soup":
      if len(dictionary[meal]) < 3:
        if product not in dictionary[meal]:
          dictionary[meal].append(product)
       
    elif meal == "Pizza":
      if len(dictionary[meal]) < 4:
        if product not in dictionary[meal]:
          dictionary[meal].append(product)
          
    elif meal == "Dessert":
      if len(dictionary[meal]) < 2:
        if product not in dictionary[meal]:
          dictionary[meal].append(product)
  
  dictionary_sorted = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))

  meals_as_list_sorted = []
  sum_of_products = 0
  for meal, products in dictionary_sorted:
    sum_of_products += len(products)
    
  if sum_of_products:  # if we have products
    for meal, products in dictionary_sorted:
      meals_as_list_sorted.append(f"{meal}:")
      for product in sorted(products):
        meals_as_list_sorted.append(f" - {product}")
  else:
    meals_as_list_sorted.append("No products in the cart!")

  return "\n".join(meals_as_list_sorted)
  
  
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))