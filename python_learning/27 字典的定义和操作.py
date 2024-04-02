# 字典：Key：Value    ：通过Key找到Value
# 字典  用{} + 键值对 组成

# 空字典定义
dict1 = {}
dict2 = dict()
print(dict1, type(dict1))
print(dict2, type(dict2))

"""
list1 = list()
tuple1 = tuple()
str1 = str()
set1 = set()
dict1 = dict()
print(list1, type(list1))
print(tuple1, type(tuple1))
print(str1, type(str1))
print(set1, type(set1))
print(dict1, type(dict1))
"""
# 字典和集合一样不可以用下标索引，只能用Key来找Value
# 除了Key不能用字典类型外，Key和Value可以用任意数据类型
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, "wo": 99}
print(dict1[1])
print(dict1[2])
print(dict1["wo"])

# 字典的嵌套
d1 = {"语文": 77, "数学": 66, "英语": 33}
d2 = {"语文": 88, "数学": 86, "英语": 55}
# d3 = {"语文": 99, "数学": 96, "英语": 66}
dict0 = {"w": d1, "z": d2, "l": {"语文": 99, "数学": 96, "英语": 66}}
print(dict0["w"])
print(dict0["w"]["语文"])

# 字典的修改或添加  字典[Key]=Value
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, "wo": 99}
dict1[1] = 11
dict1[5] = 100
print(dict1)

# 删除元素
dict1 = {1: 10, 2: 20, 3: 30, 4: 40}
a = dict1.pop(3)
print(a)   # print(dict1.pop(3))   不知道为什么不行
print(dict1)
# 清空字典
print()
dict1 = {1: 10, 2: 20, 3: 30, 4: 40}
dict1.clear()
print(dict1)
# 获得所用Key（为了遍历字典）
dict1 = {1: 10, 2: 20, 3: 30, 4: 40}
a = dict1.keys()
print(a)
# 遍历字典 统计字典元素数量(len())
# 方法1
for x in a:
    print(dict1[x])
# 方法2
for key in dict1:  # 直接遍历字典就行
    print(dict1[key])

y = len(dict1)
print(y)

# 作业
dict8 = {
         "1": {"部门": "科技部", "工资": 3000, "级别": 1},
         "2": {"部门": "市场部", "工资": 5000, "级别": 2},
         "3": {"部门": "市场部", "工资": 7000, "级别": 3},
         "4": {"部门": "科技部", "工资": 4000, "级别": 1},
         "5": {"部门": "市场部", "工资": 6000, "级别": 2}
         }
for key in dict8:
    if dict8[key]["级别"] == 1:  # 可以用（变量）=dict8[key]["级别"]接受内部小字典
        dict8[key]["工资"] += 1000
        dict8[key]["级别"] += 1
print(dict8)
print(dict8)  # 鼠标双击选中目标

# 统计容器最大/最小元素：max(容器), min(容器)
# 容器的通用转化功能list() tuple() str() set()
# 容器通用排序功能：sorted(容器,reverse=True)  # reverse默认为False,排序的结果会变为列表
name = "xiaoxiao"
print(sorted(name))
name2 = [2, 3, 4, 1]
print(sorted(name2))
print(sorted(name2, reverse = True))  # reverse=True：表示反转为真

# 字符串的比较是按ASCII码比较的
# 字符串是按位比较,也就是一位位进行对比,只要有一位大,那么整体就大。
# 如"abc" < "abd" ; "ab" > "a"
if "abc" < "abd":
    print("1")
else:
    print("2")
print("ab" > "a")
print("key1" > "key2")

# 老师用的截图软件：snipaste