# 10天每天吃三顿
i = 1
while i <= 10:
    print(f"第{i}天")
    j = 1
    while j <= 3:
        print(f"第{j}顿饭")
        j += 1
    i += 1
print(f"第{i-1}天结束")
m = i-1
# tips
# print不换行加，end=''
print("hello", end='')
print("world")
# \t(制表符)：单词对齐功能
print("he\tis")
print("she\tis")

# 打印九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f"{i}*{j}={i*j}\t", end='')
        i += 1
    print()  # 换行
    j += 1
