# 公元年分除以4不可整除，為平年。
# 公元年分除以4可整除但除以100不可整除，為閏年。
# 公元年分除以100可整除但除以400不可整除，為平年。
# 公元年分除以400可整除但除以3200不可整除，為閏年。

# 應該都對吧 ＸＤ
def is_leap(year):
    return year % 4 == 0 and year % 3200 != 0


year = input('input year: ')
year = int(year)
print('is leap ? ', is_leap(year))
