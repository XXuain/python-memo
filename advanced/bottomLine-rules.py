# naming convention
# _, _name, name_, __name, __name__

# _ 臨時 不重要的變數
for _ in range(10):
    print(_, 'hi')

name, _ = 'name$age'.split('$')

# public, _private


def f():
    print('public')


def _ff():  # import * 才有用
    print('private')


class Friend:
    def public_fun(self):
        print('public_fun')

    def _private_fun(self):
        print('private_fun')


# name_ 避免 keyword
class_ = 'class'


# __name 重新命名
class Person:
    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1


p = Person()
print(dir(p))
print(p.x)
print(p._y)
print(p.__z)  # 會出錯
