"""
列表的方法包括：
插入元素
删除元素
清空列表
修改元素
统计元素个数
"""
# （1）函数：通过“函数名（）”的方式进行调用。
# （2）方法：通过“对象.方法名”的方式进行调用。
# list就是 一个类 list.··就是方法
# 定义在类中的函数称为方法
# 函数和方法的调用方式不同，书写方式不同
"""
方法：
class Student:
    def add(self, x, y):
        return x + y
函数调用：num = add(1, 2)
方法调用：student = Student()
        num = student.add(1, 2)
"""
# 0 空列表定义
list90 = []
list91 = list()
# 1 列表查询功能
list1 = [1, 2, 3]
a = list1.index(2)  # index称为方法
print(a)

# ctrl + f :搜索
# 2 列表的修改功能
list1[2] = "9"
print(list1)

# 3 列表插入功能
list1 = [1, 2, 3]
list1.insert(1, 1.5)  # (下表, 元素)
print(list1)

# 4 追加元素到列表尾部
list1 = [1, 2, 3]
list1.append(4)  # append 附加
print(list1)

# 5 追加一批元素到尾部extend(其他数据容器) 如：extend([1, 2, 3])
list2 = [2, 3, 4]
list2.extend([5, 6, 7])
print(list2)

# 6 删除元素
# del 列表[下标]  或   列表.pop(下标)
print()
list2 = [2, 3, 4]
del list2[0]
print(list2)
x = list2.pop(1)  # 方法pop可以取出元素（有返回值即取出的元素）
print(list2, x)

# 删除某元素在列表的第一个匹配项
list2 = [2, 3, 4, 2]
list2.remove(2)
print(list2)

# 7 清空列表
list2.clear()
print(list2)

# 统计某元素在列表中的数量
list3 = [7, 5, 6, 7]
print(list3.count(7))

# 8 列表元素个数
print(len(list3))

# 练习
print()
list9 = [21, 25, 21, 23, 22, 20]
list9.append(31)
list9.extend([29, 33, 30])
print(list9.pop(0))
print(list9.pop(8))  # print(list9.pop(-1)) 用-1更好
print(list9.index(31))
print(list9)
