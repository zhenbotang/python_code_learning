# indent expected：缩进错误
# statement expected：语法错误
# 条件
# 身高小于120/vip等级大于3免费，否则付费10元
if int(input("输入身高")) > 120:
    # print("身高要求不达标")
    if int(input("输入vip等级")) > 3:
        print("vip大于3，免费")  # if和else后面的print要缩进别忘了
    else:
        print("需要付费10元")
else:
    print("身高达标，免费游玩")

# 条件
# 1.年龄大于等于18且小于30
# 2.入职时间大于2年或级别大于3
if 30 > int(input("输入你的年龄")) >= 18:
    if int(input("输入你的入职时间（年）")) > 2:
        print("满足条件")
    elif int(input("输入的的级别")) > 3:
        print("满足条件")
    else:
        print("不满足条件")
else:
    print("不满足条件")

# tap=四个空格
# if作业
# 随机生成1-10的数字，三次机会猜数字，要提示大了或小了

import random
num = random.randint(1, 10)
# print(num)
guess_num = int(input("输入第一次猜测"))
if guess_num > num:
    print("太大了")
    guess_num = int(input("输入第二次猜测"))
    if guess_num > num:
        print("还是太大了")
        if int(input("输入第三次猜测")) == num:
            print("第三次猜对了")
        else:
            print("三次都错了")
    elif guess_num < num:
        print("这次太小了")
        if int(input("输入第三次猜测")) == num:
            print("第三次猜对了")
        else:
            print("三次都错了")
elif guess_num < num:
    print("太小了")
    guess_num = int(input("输入第二次猜测"))
    if guess_num < num:
        print("还是太小了")
        if int(input("输入第三次猜测")) == num:
            print("第三次猜对了")
        else:
            print("三次都错了")
    elif guess_num > num:
        print("这次太大了")
        if int(input("输入第三次猜测")) == num:
            print("第三次猜对了")
        else:
            print("三次都错了")
else:
    print("一次猜对")

# 改进
import random  # 只需要写一次
num = random.randint(1, 10)
guess_num = int(input("输入第一次猜测"))
if guess_num == num:
    print("第一次猜对了")
else:
    if guess_num > num:
        print("太大了")
    else:
        print("太小了")
    guess_num = int(input("输入第二次猜测"))
    if guess_num == num:
        print("第二次猜对了")
    else:
        if guess_num > num:
            print("太大了")
        else:
            print("太小了")
        guess_num = int(input("输入第三次猜测"))
        if guess_num == num:
            print("第三次猜对了")
        else:
            print("很遗憾，三次全错")
# 36行变23行，先判断==
