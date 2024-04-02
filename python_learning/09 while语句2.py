# 任务：猜1-100数字，次数不限，输出猜测次数
import random
num = random.randint(1, 100)
print(num)
guess_num = int(input("输入猜测的数字"))
times = 1
while guess_num != num:
    if guess_num > num:
        print("太大了")
    else:
        print("太小了")
    guess_num = int(input("再次输入猜测的数字"))
    times += 1
print(f"猜对了，答案是{guess_num},一共猜了{times}次")

# 黑马的
count = 0
flag = True
while flag:
    guess_num = int(input("输入猜测的数字"))
    count += 1
    if guess_num == num:
        print("猜对了")
        flag = False
    else:
        if guess_num > num:
            print("太大了")
        else:
            print("太小了")
print(f"一共猜了{count}次")
