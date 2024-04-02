"""
if 用于有限次数的循环
while 用于随机或不限次数的循环
for循环语句，本质上是遍历：序列类型
"""

"""
for 临时变量 in 待处理数据集
待处理数据集为序列类型，包括 字符串 列表 元组
"""

# range（数字序列）左闭右开
# range(10) 0-9的序列 也是10个数字
for x in range(5):
    print(x, end='')
print()  # 换行

for x in range(2, 5):
    print(x, end='')
print()

# for x in range(num1, num2, step):   (step 步长)
for x in range(2, 10, 2):
    print(x, end='')
print()

# for + range(num) 可以实现while的自定义循环次数的循环
for x in range(3):
    print("送东西")
# 通过range快速锁定for的循环次数

# 作业（得出数字序列中几个偶数）
num = 100
num_2 = 0
for x in range(1, num):
    if x % 2 == 0:   # 等于即比较即==
        num_2 += 1
print(num_2)
# print(x)
# 临时变量x，在编程规范上作用于for循环内部，不建议在外部使用内部循环的循环变量
# 真的要用到临时变量需要在循环外部先定义好临时变量，循环后变量会被覆盖
print()
i = 0
for i in range(5):
    print(i)
print(i)
