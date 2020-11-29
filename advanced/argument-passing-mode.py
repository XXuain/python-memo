# pass by value
# pass by reference
# pass by object reference
# dynamic bindin

def f(y):
    y.append(1)


x = [0]
f(x)
print(x)  # [0] || [0,1]


def ff(y):
    y += 1  # 遇到設值指令 會重新導向


x = 0
ff(x)
print(x)  # 0 || 1
