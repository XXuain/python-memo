# 找出清單中最大數
# 回傳最大數，清單為空回傳 0

def find_max1(a_list):
    if len(a_list) == 0:
        return 0
    return max(a_list)


def find_max2(a_list):
    if not a_list:  # 檢查a_list清單有沒有東西
        return 0

    max = a_list[0]
    for num in a_list:
        if max < num:
            max = num
    return max


print(find_max1([1, 2, 900, 2]))
print(find_max2([1, -600, 600, 2]))
