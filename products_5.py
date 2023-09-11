#如何清單裝兩種東西
#大清單中裝小清單

products = []

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

# 每一個小清單的第x格資料印出來
for p in products:
    print(p[0], '的價格是', '$', p[1])

with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

#如果沒有這個檔案會create
#如果有這個檔案會覆蓋
#逗號會將CSV分格隔開

#字串可以 + / *

    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]

# 把大清單中每一個小清單印出來
# for product in products:
#     print(product)

# products[0][0]