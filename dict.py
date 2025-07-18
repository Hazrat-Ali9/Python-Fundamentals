shoppingcart = dict()

shoppingcart['milk'] = 3
shoppingcart['yoghurt'] = 2
shoppingcart['coffe'] = 1
shoppingcart['potato'] = 2
shoppingcart['tomato'] = 2
shoppingcart['banana'] = 2.5

print(shoppingcart)

print("key and values in the dictionary:",shoppingcart.items(),"\n")
print(shoppingcart.popitem(),"\n")

print(shoppingcart.pop('tomato'))
# print(dir(shoppingcart))
