def shopping_list(budget, **kwargs):
  if budget < 100:
    return "You do not have enough budget."

  result = ""

  count_of_bought_products = 0

  for product_name, price_quantity in kwargs.items():
    total_price = price_quantity[0] * price_quantity[1]
    if total_price <= budget:
      count_of_bought_products += 1
      budget -= total_price
      result += f"You bought {product_name} for {total_price:.2f} leva.\n"
    
    if count_of_bought_products == 5:
      break

  return result