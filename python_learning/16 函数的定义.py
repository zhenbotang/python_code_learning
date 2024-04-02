"""
函数的定义
def 函数名(传入参数):
    函数体
    return 返回值
"""

def guess():
    print("hello\nwhere are you from")
guess()
# "\n":字符串内换行
# 简单函数的参数或者返回值如果不需要可以不用定义
def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count
print(my_len("python"))

def add(x, y):  # x和y是形式参数（形参）6和1是实际参数（实参）
    result = x + y
    return result
print(add(6, 1))

# 作业：是否发烧检测
def temperature(x):
    if x > 37.5:
        print("发烧")
    else:
        print("体温正常")
temperature(int(input("输入你的体温")))
temperature(37)

def add(x, y):
    result = x + y
    print("111")
    return result
print(add(6, 1))
# print()等要写在return前面，函数遇到return就结束了，return后面的不执行
