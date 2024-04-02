# function 函数
def func_a(a, b):
    result_1 = a + b
    return result_1


# expected 2 blank lines，found (需要两条空白行，发现0条)
# 函数上面和下面都要空两行就不会提醒
def func_b(a, b):
    result_2 = a * b
    return result_2


def func_c(a, b):
    result_3 = func_a(a, b) + func_b(a, b)
    return result_3


print(func_a(2, 3))
print(func_b(2, 3))
print(func_c(2, 3))
"""
局部变量和全局变量
函数内部的变量result_1（2，3）是局部变量，只在函数体内部生效
局部变量在函数内部临时保存数据，调用完成后变量就被销毁了
定义在函数外面的变量就是全局变量
"""
# tips：快速注释首尾段不需要全部选中
# 函数内部变量（局部变量 ）的定义不影响全局变量，同名也不影响
num = 200
def a():
    print(num)
def b():
    # global num  加上global后可以在函数内部定义全局变量，此时会修改 外部的num
    num = 500  # 局部变量
    print(num)
a()
b()
print(num)

print()
num = 200
def a():
    print(num)
def b():
    global num  # 加上global后可以在函数内部定义全局变量，此时会修改外部的num
    num = 500   # 全局变量 global（整体的，全球的）
    print(num)
a()
b()
print(num)
