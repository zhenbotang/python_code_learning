# 数据输出print()
# 数据输入input() 会把输入转化成字符串
# print("告诉我你的名字")
# name = input()
#
name = input("告诉我你的名字")
print(f"欢迎你{name}")
num = input("你的密码是")
print(f"你的密码类型是{type(num)}")
num = int(num)
print(f"你的密码类型是{type(num)}")
# 作业
user_name = input("你的姓名")
user_type = input("你的用户类型")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎你的光临")
