# 数据输出print()
# 数据输入input() 输入会转化为字符串
"""
print("告诉我你的名字")
name = input()
print("欢迎你", name)
"""
name = input("告诉我你是谁")
print(f"欢迎你{name}")
num = input("输入密码")
num = int(num)
print(f"密码类型是:{type(num)}")
print("密码类型是:", type(num))
# 作业
user_name = input("姓名")
user_type = input("用户类型")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎您的光临")
