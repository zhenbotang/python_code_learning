"""
为了得到一个针对特定需求、可供重复利用的代码段
提高程序的复用性,减少重复性代码,提高开发效率
所以使用函数
"""

name = "python"

# 不用内置代码
count = 0
for i in name:
    count += 1
print(count)

# 用内置代码len()
length = len(name)
print(length)

# 用自己定义的代码
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串的长度为{count}")
my_len("python")
