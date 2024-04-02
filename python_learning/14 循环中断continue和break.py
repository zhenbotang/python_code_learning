# continue 临时跳过，break 直接结束
# 可用于for和while循环中
for x in range(5):
    print("1")
    continue
    print("2")

print()
for x in range(5):
    print("1")
    break
    print("2")

# continue和break只对本层循环有效
print()
for i in range(5):
    print("1")
    for j in range(5):
        print("2")
        continue
        print("3")
    print("4")

print()
for i in range(5):
    print("1")
    for j in range(5):
        print("2")
        break
        print("3")
    print("4")

# This code is unreachable 无法访问此代码
# 作业
# 要求 公司有10000元给20个员工发工资
#      编号1-20，没人1000元，当绩效低于5时不能领取，工资发完就结束
import random
num_wage = 10000
for i in range(1, 21):
    num_goal = random.randint(1, 10)
    if num_goal < 5:
        print(f"第{i}名员工绩效低于5，不发工资")
    else:
        print(f"第{i}名员工绩效高于5，发表1000元工资")
        num_wage -= 1000
    if num_wage == 0:
        print(f"到第{i}名员工为止，工资全部发完")
        break

# 我的不好，变量（总工资，每人工资，人数变代码会错误）
# 黑马的
print()
import random
num_wage = 10000
for i in range(1, 21):
    num_goal = random.randint(1, 10)
    if num_goal < 5:
        print(f"第{i}名员工绩效低于5，不发工资")
        continue
    if num_wage >= 1000:
        num_wage -= 1000
        print(f"第{i}名员工绩效高于5，发表1000元工资")
    else:
        print(f"余额不足，剩余{num_wage},下次一定")
        break
