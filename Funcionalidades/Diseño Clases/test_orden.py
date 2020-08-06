from producto import Product
from orden import Order

product1 = Product('Pasta Fresa', 2.00)
product2 = Product('Pasta Rellena', 3.00)
product3 = Product('Pasta Cremosa', 2.80)
product4 = Product('Pasta Seca', 1.90)


products = (product1, product2, product3, product4)
order = Order()
for i in range(len(products)):
    order.add_product(products[i])

print(order)
price_total = order.calc_total()
print('El precio total es: ' + str(price_total))

lista = order.get_products()

for i in lista:
    print(i)











