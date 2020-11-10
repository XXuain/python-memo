import os


def open_file(fileName):  # 開啟檔案
    chatData = []
    with open(fileName, 'r', encoding='UTF-8-sig') as file:  # 打開記事本的編碼
        for f in file:
            chatData.append(f.strip())
    return chatData


def format_data(chatData):
    new_data = []
    person = None
    for c in chatData:
        if c == 'Allen' or c == 'Tom':
            person = c
            continue
        new_data.append(person + ': ' + c)
    return new_data


def write_file(fileName, chatData):
    with open(fileName, 'w', encoding='utf-8') as file:
        for c in chatData:
            file.write(c + '\n')


def main():
    orangeFileName = 'input.txt'
    if os.path.isfile(orangeFileName):
        chatData = open_file(orangeFileName)
        format_chat_data = format_data(chatData)
        write_file('output.txt', format_chat_data)
    else:
        print('have error')


main()
