# 序列（列表，元组，字符串 ）的切片也是新得到的
# 语法：序列（起始下标：结束下标：步长）
# 起始下标留空表示从头开始，结束下标留空表示到结尾
name = "123123"
name2 = name[::2]
print(name2)
name3 = name[2:5]  # 下表2开始5结束（不包括5）
print(name3)
# 步长可以是负数
name4 = name[::-1]  # 反转序列
print(name4)

# 切片作业
x = "练习案例，切片实践，任意方法"
print(x[-6])
y = x[5:9][::-1]  # y = x[x.index("践"):x.index("，"):-1]
print(y)          # y = x[::-1][5:9]

# TypeError: slice indices must be integers or None or have an __index__ method
# TypeError：切片索引必须是整数或None，或者具有__index__方法
