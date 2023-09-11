#如何清單裝兩種東西
#大清單中裝小清單

products = []

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    products.append([name, price])
print(products)

# products[0][0]