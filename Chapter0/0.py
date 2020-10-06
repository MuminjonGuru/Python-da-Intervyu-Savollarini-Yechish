for item in basket1:
  if item in basket2:
    basket2.remove(item)

print('Basket1:' + basket1)
print('Basket2:' + basket2)

while len(basket1) > len(basket2):
  item_to_transfer = basket1.pop()
  basket2.append(item_to_transfer)

print('Basket1: ' + basket1)  
print('Basket2: ' + basket2)
