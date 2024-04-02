# 编码技术：翻译规则（如何将内容翻译为二进制）
# UTF-8为主要编码格式，基本一律以UTF-8进行文件编码
# 文件可以（打开 关闭 读 写）
import time

# open()打开或创建文件
# open(name,mode,encoding)
# name：文件名的字符串（可包含路径）
# mode：打开文件的模式（只读r 写入w 追加a） a：append
# encoding：编码格式（UTF-8）

f = open("D:/text.txt", "r", encoding="UTF-8")  # 前两个是位置参数，encoding是关键字参数
content = f.read(2)  # read()不填数字读全部，连续读取会记录位置
print(content)

content2 = f.readlines()  # readlines()读取全部行，返回一个列表，一行为一个元素
print(content2)
f.close()
# \n:换行符
# readline()读一行内容
print("-------")
f = open("D:/text.txt", "r", encoding="UTF-8")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()

# for循环读取内存（一行一行）
f = open("D:/text.txt", "r", encoding="UTF-8")
for line in f:
    print(f"本行的内容是：{line}")
f.close()
# time.sleep(50000)   5w秒

# with open 语法：操作完成后自动关闭文件
print("----")
with open("D:/text.txt", "r", encoding="UTF-8") as f:
    a = f.read(2)
    print(a)

# 作业：输出文本到文件中
# p24字符串的分割和计数
# 方法一
print("--------------------------------------")
with open("D:/text2.txt", "r", encoding="UTF-8") as f2:
    content2 = f2.read()
    print(content2)
    a = content2.count("itheima")
print(a)

# 方法二
print()
count = 0
with open("D:/text2.txt", "r", encoding="UTF-8") as f2:
    for line in f2:
        line2 = line.strip()  # 直接用strip()什么都不加就是去重开通要结尾的空格和换行符
        print(line2)
        a = line2.split(" ")  # 去除/n用replace或strip
        print(a)
        for word in a:
            if word == "itheima":
                count += 1
print(count)
