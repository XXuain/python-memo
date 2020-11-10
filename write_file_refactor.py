import os  # 作業系統模組 operating system


def read_file(fileName, products):  # 檢查檔案是否存在
    # 讀取檔案
    with open(fileName, 'r', encoding='utf-8') as file:
        for f in file:
            if '商品,價格' in f:
                continue  # 繼續
            name, price = f.strip().split(',')  # split 會將區塊變成清單
            products.append([name, price])
    return products


def user_input(products):  # 讓使用者輸入
    while True:
        name = input('product name: ')
        if name == 'q':
            break
        price = input('product price: ')
        products.append([name, price])

    # 印出所有購買紀錄
    print(products)
    for p in products:
        print(p[0], 'price is: ', p[1])
    return products


def write_file(fileName, products):  # 寫入檔案
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write('商品,價格\n')
        for f in products:
            file.write(f[0] + ',' + f[1] + '\n')  # csv 用逗點做區隔


def main():
    fileName = 'products.csv'
    products = []
    if os.path.isfile(fileName):
        products = read_file(fileName, products)
    products = user_input(products)
    write_file(fileName, products)


main()
