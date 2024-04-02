# 将容器内元素依次取出处理的行为叫：遍历、迭代
# 列表的遍历-while循环
def list1_func():
    list1 = [1, 2, 3, 3]
    index = 0
    while index < len(list1):
        element = list1[index]
        index += 1
        print(f"列表的元素有：{element}")


list1_func()


# 列表的遍历-for循环
def list2_func():
    list2 = [9, 2, 3, 3]
    for element in list2:
        print(f"列表的元素有：{element}")


print()
list2_func()

# while循环可以自定循环条件，for循环不可以自定
# while可以用在任意循环场景，for只能一个个遍历数据容器
# 但for使用 更方便，用的多
# for简单 while灵活

# 作业
# 把列表6的偶数加入到列表7,8中
list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list7 = []
for x in list6:
    if x % 2 == 0:
        list7.append(x)
print(list7)

index2 = 0
list8 = []
while index2 < len(list6):
    if list6[index2] % 2 == 0:
        list8.append(list6[index2])
    index2 += 1    # 这个是与while绑定的，在while的同一级下面！！！
print(list8)

list = [1, 2]
print(list)  # list是一个内置的函数，取变量名最好不要用内置函数。
