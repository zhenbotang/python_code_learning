# 元组与列表类似，不同点是元组不可以被修改
# 元组 == 只可以读的列表
# 空元组
t1 = ()
T2 = tuple()
print(t1, T2)

t3 = (1, "2", True)
print(t3, type(t3))

# 若元组只有一个元素需要加逗号
t4 = (1,)
t5 = (1)   # Remove redundant parentheses 删除多余的括号
print(t4, type(t4))
print(t5, type(t5))

# 元组的嵌套
t6 = ((1, 2, 3), (4, 5, 6))
print(t6, type(t6))

# 元组下标索引读出元素
num = t6[1][2]
print(num)

# 元组可以 (检索 计数 计算长度)
print()
t7 = (9, 8, 3, 4, 2, 9)
print(t7.index(9))   # 只检索到左到右的第一个元素9
print(t7.count(9))
print(len(t7))

list7 = [1, True]
list8 = [0, False]
print(list7.count(1))
print(list8.count(0))  # True计为1，False计为0

# 元组的遍历
print()
t8 = (9, 8, 3, 4, 2, 9)
index = 0
while index < len(t8):
    print(f"元组的元素为：{t8[index]}")
    index += 1
print()
for x in t8:
    print(f"元组的元素为：{x}")

# 元组内的list的值可以修改, list还是list，只是值变了
t9 = (1, 2, [3, 4])
print(t9)
t9[2][0] = 5
t9[2][1] = 6
print(t9)

# 作业
tuple1 = ('周杰伦', 11, ['football', 'music'])
print(tuple1.index(11))
print(tuple1[0])
tuple1[2].pop(0)  # del tuple1[2][0] (先选中列表)
tuple1[2].append("coding")  # 元组内列表的修改要先选中列表：元组名[列表位置]
print(tuple1)
