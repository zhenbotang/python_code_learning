"""
数据容器：可以储存多个元素的数据类型
包括 list（列表）  tuple（元组） str（字符串） set（集合） dict（字典）
"""
# 列表  ['1', 2, True]
# 如班级学生姓名可以用列表
name = ['1', 2, True]  # 列表可以存任意数据类型
print(name, type(name))
name2 = ['1', 2, True, name]
print(name2)  # 列表可以嵌套

# list下标索引
# 左到右是0 1 2···，右到左是-1 -2 -3···
print(name2[0])
print(name2[1])
print(name2[2])
print(name2[3])
print()
print(name2[-1])
print(name2[-2])
print(name2[-3])
print(name2[-4])
print()
print(name2[3][2])
