# 大作业：ATM取款机
money = 5000000                          # 500w
name = input("请输入你的姓名")


def check(show_head):
    if show_head:
        print("----------------查询余额----------------")
    print(f"{name}，您好，您的余额剩余：{money}元")


def deposit(a):
    global money
    money = money + a
    print("-----------------存款-----------------")
    print(f"{name}，您好，您存款{a}元成功")
    check(False)


def withdraw(b):
    global money
    money = money - b
    print("-----------------取款-----------------")
    print(f"{name}，您好，您取款{b}元成功")
    print(f"{name}，您好，您的余额剩余：{money}")


num = None  # 函数内使用要先在外部定义


def main():
    global num
    print("----------------主菜单----------------")
    print(f"{name},您好，欢迎来到黑马银行ATM机，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款 \t[输入2]")
    print("取款 \t[输入3]")
    print("退出\t\t[输入4]")  # 对其距离太大要（加一个空格 或 两个\t）
    num = int(input("请输入您的选择"))


# 无限次数，用while True，退出break
while True:
    main()
    if num == 1:
        check(True)
        continue
    elif num == 2:
        deposit(int(input("输入存款值")))  # 运用函数时括号内要输入实参而不是形参
        continue
    elif num == 3:
        withdraw(int(input("输入取款值")))
        continue
    else:
        print("程序退出")
        break

# main()
# for x in range(1, 101):
#     if num == 1:
#         check(True)
#         main()
#     elif num == 2:
#         deposit(int(input("输入存款值")))  # 运用函数时括号内要输入实参而不是形参
#         main()
#     elif num == 3:
#         withdraw(int(input("输入取款值")))
#         main()
#     elif money < 0:
#         break
#     else:
#         break