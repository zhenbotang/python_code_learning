# 如字符串"python"是python中每个字母的集合，所以字符串也是数据容器
# 字符串和元组一样不可修改
name = "pytho n"
print(name[0])
print(name[-2])  # 空格也计数
print(name[-1])

name2 = "you and me"
a = name2.index("and")  # 空格计算
print(f"and在字符串中的起始位置为{a}")

# 字符串的替换
# 字符串的replace方法，是得到一个新的字符串（即返回值），原字符串不变
new_name2 = name2.replace("and", "or")  # replace后直接生成表达式
print(name2)
print(new_name2)

# 字符串的分割split
# 以选定分隔符字符串，将字符串分为多个字符串，并存入列表
list1 = name2.split(" ")
print(list1)

# 字符串的规整strip()【有默认值参数：空格】去前后空格
name3 = "  you and me  "
print(name3)
print(name3.strip())
name4 = "12 236 12"
print(name4)
print(name4.strip("12"))  # 1和2不分前后都去除

# count和len
print()
name5 = "you and you"
print(name5.count("you"))
print(len(name5))

# 字符串的遍历
name9 = "黑马程序  员"
index = 0
while index < len(name9):
    print(f"name9的元素为：{name9[index]}")
    index += 1
print()
for x in name9:
    print(f"name9的元素为：{x}")

# 作业
h = "itheima itcast boxuegu"
print(h.count("it"))
print(h.replace(" ", "|"))  # shift + 反斜杠就是竖线
print(h.split("|"))
