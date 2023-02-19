from collections import deque
ramens = deque(int(i) for i in input().split(", "))  # pop
customers = deque(int(i) for i in input().split(", ")) # popleft

while ramens and customers:
  current_ramen = ramens.pop()
  current_customer = customers.popleft()

  if current_ramen == current_customer:
    continue
  elif current_ramen > current_customer:
    current_ramen -= current_customer
    ramens.append(current_ramen)
  elif current_customer > current_ramen:
    current_customer -= current_ramen
    customers.appendleft(current_customer)


if not customers:
  print("Great job! You served all the customers.")
  if ramens:
    print(f"Bowls of ramen left: {', '.join(str(ramen) for ramen in ramens)}")
else:
  print("Out of ramen! You didn't manage to serve all customers.")
  print(f"Customers left: {', '.join(str(customer) for customer in customers)}")