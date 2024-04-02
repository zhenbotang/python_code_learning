# 捕获语法
# try:
#   可能发生错误的代码
# except:
#   如果出现异常执行的代码
# 基本语法
try:
    f = open("D:/abc.txt", "r", encoding="UTF-8")
except:
    f = open("D:/abc.txt", "w", encoding="UTF-8")
# 捕获指定异常
try:
    print(name)
except NameError as error1:
    print("出现变量未定义异常")
    print(error1)
# 捕获多个异常（多个异常用元组写）
try:
    print(name)
except (NameError or ZeroDivisionError) as error1:
    print("出现变量未定义或除0异常")
    print(error1)
# 捕获所有异常
try:
    print(name2)
except Exception as error2:  # Exception是顶级异常
    print("op")
# else用法
try:
    print(1)
except:
    print("出现异常")
else:
    print("没有出现异常")  # 没出现异常会执行else
# finally用法
try:
    print(1)
except:
    print("出现异常")
else:
    print("没有出现异常")  # 没出现异常会执行else
finally:
    print("结束")  # 有无异常都会在最后执行，一般用于关闭资源文件

print("---")
# 异常的传递性
def func1():
    print("开始func1")
    num = 1/0
    print("结束func1")
def func2():
    print("开始func2")
    func1()
    print("结束func2")
# def main():
#     func2()
#     print(3)
# main()
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常为{e}")
main()
