class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):  # 顯示簡易版 可讀性高，有用資訊
        # return self.name + ' $' + str(self.price)
        return f'{self.name} ${self.price}'

    def __repr__(self):  # 顯示詳細版 可用 print(repr(CLASS))
        return f'<Product({self.name}, ${self.price}) >'


p = Product('水果茶', 80)
print(p)
print(repr(p))
