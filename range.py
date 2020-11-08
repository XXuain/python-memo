# range 清單產生器
range(5) #[0, 1, 2, 3, 4]
range(3, 8) #[3, 4, 5, 6, 7] 包含開始值，不包含結束值
range(2, 10, 3) #[2, 5, 8] 開始值加3(遞增值)

import random
for i in range(50):
  r = random.randint(3,333)
  print('這是第', i, '幾次', '產生隨機數：', r)
