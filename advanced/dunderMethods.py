class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):  # 顯示簡易版 可讀性高，有用資訊
        # return self.name + ' $' + str(self.price)
        return f'{self.name} ${self.price}'

    def __repr__(self):  # 顯示詳細版 可用 print(repr(CLASS))
        return f'<Product({self.name}, ${self.price}) >'

    def __add__(self, other):
        if isinstance(other, str):  # 如果 other 是 字串的實例
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        res = []
        if isinstance(other, int):
            for _ in range(other):
                res.append(self)
        return res


p1 = Product('水果茶', 80)
p2 = Product('義大利麵', 200)
p1 + '檸檬'
print(p1 + p2)
print(p1 * 5)
print(p1)
# print(repr(p))
