products = []
while True:
    name = input('product name: ')
    if name == 'q':
        break
    price = input('product price: ')
    products.append([name, price])

print(products)
for p in products:
    print(p[0], 'price is: ', p[1])

with open('products.csv', 'w', encoding='utf-8') as file:
    file.write('商品,價格\n')
    for f in products:
        file.write(f[0] + ',' + p[1] + '\n')  # csv 用逗點做區隔
