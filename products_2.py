#如何清單裝兩種東西
#大清單中裝小清單

products = []

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)

# 每一個小清單的第x格資料印出來
for product in products:
    print(product[0], '的價格是', '$', product[1])

    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]

# 把大清單中每一個小清單印出來
# for product in products:
#     print(product)

# products[0][0]