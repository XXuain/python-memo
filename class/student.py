# class 類別(總類)

class Student:
    def __init__(self, name):
        print('be born')
        self.myName = name

    def do_hw(self):
        print('do homework')
        self.study('English book')

    def study(self, bookName):
        print('im studing', bookName)


s1 = Student('ming')
s2 = Student('betty')

print(s1.myName, s2.myName)
print(dir(s1))  # 印出物件屬性
