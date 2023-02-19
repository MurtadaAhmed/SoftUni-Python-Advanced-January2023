from collections import deque
pizzas = deque(int(i) for i in input().split(", "))  # popleft
employees = deque(int(i) for i in input().split(", "))  # pop

pizzas_made = 0
MAXIMUM_PIZZAS = 10

while pizzas and employees:
  current_order = pizzas.popleft()
  if current_order <= 0 or current_order > MAXIMUM_PIZZAS:
    continue

  employee = employees.pop()

  if current_order <= employee:
    pizzas_made += current_order
  else:
    pizzas_made += employee
    current_order -= employee
    pizzas.appendleft(current_order)
  

if not pizzas:
  print(f"""All orders are successfully completed!
Total pizzas made: {pizzas_made}
Employees: {', '.join(str(employee) for employee in employees)}""")
else:
  print(f"""Not all orders are completed.
Orders left: {', '.join(str(pizza) for pizza in pizzas)}""")