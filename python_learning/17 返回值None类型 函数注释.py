"""
无返回值时返回值为None
None使用场景
1 函数返回值
2 if判断
3 变量定义
"""
def da():
    print("打印")
da()
i = da()
print(i, type(i))

def check_age(x):
    if x > 18:
        print("success")
        return "success"
    else:
        return None
# check_age(19)  只调用函数是不输出return的结果的要用变量接收然后print
result = check_age(12)
print(result)

# if语句中,None == False,not None == True
# if语句判断为真才会继续执行
if not result:
    print("未成年人禁止进入")

# None可以声明无初始值的变量（暂时用None）
name = None
print(name)

# param（parameter）参数
# 函数的说明文档格式
def add(x, y):
    """
    函数说明
    :param x:形式参数1
    :param y:形式参数2
    :return:返回值为1，2相加
    """
    result_2 = x + y
    return result_2

# add()  # 悬停可以查看函数注释
