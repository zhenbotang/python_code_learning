# bool是数据类型，包括True和False
result1 = 10 > 5
result2 = 'a' == 'b'
print(result1, result2, type(result1), type(result2))
# '==':判断是否相等，== < > >= <= !=(是否不相等)是比较运算符
# bool数据类型的两个字面量：False True
bool_1 = True
print(bool_1, type(bool_1))
# if后加冒号，结果句4个空格缩进
age = 10
if age > 5:
    print("ok")
    print("okk")
if True:
    print("okkk")  # 原因：单词拼写检查功能，说明当前拼写有问题，
#                    解决方式：按照驼峰命名法，重新命名即可
# 作业
print("欢迎来到游乐园，儿童免费，成人收费")
age = input("请输入你的年龄")
age = int(age)
# age = int(input("请输入你的年龄"))
if age >= 18:
    print("您已经成年，游玩需要补票10元")
else:
    print("您未成年，免费游玩")
print("祝您游玩愉快")
# 作业2
print("欢迎来到动物园")
height = int(input("请输入你的身高（cm）"))
if height > 120:
    print("您的身shen高超过120cm，游玩需要购票10元")
else:
    print("您的身高未超过120cm，可以免费游玩wan")
print("祝你游玩愉快")

# if elif else语句 各个语句间互斥，即只能执行一条结果，也可以不写else
height = int(input("输入你的身高（cm）："))
vip_level = int(input("输入你的vip等级（1-5）："))
if height < 120 and vip_level > 3:
    print("你的身高不到120cm，且vip等级大于3，可以免费游玩")
elif height < 120:
    print("你的身高不到120cm，可以免费游玩")
elif vip_level > 3:
    print("你的vip等级大于3，可以免费游玩")
else:
    print("你需要付费10元游玩")
# ctrl+/快速注释，下面是不使用变量的写法，功能也有所不同，不用输入全部量，满足前面的就不用输入后面的
if int(input("输入你的身高（cm）：")) < 120:
    print("你的身高不到120cm，可以免费游玩")
elif int(input("输入你的vip等级（1-5）：")) > 3:
    print("你的vip等级大于3，可以免费游玩")
else:
    print("需要购票 10元")
# 作业
num = 10
if int(input("请输入猜想的数字")) == num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次")) == num:
    print("恭喜你猜对了")
elif int(input("不对，最后一次")) == num:
    print("恭喜你猜对了")
else:
    print("Sorry,全部猜错了，数字为10")
# if 10 == 10：（':'expected:表示冒号输入错误）
