print(type(9))
# 可以用变量存储type()的结果
m = type("一")
print(m)
print(type(11.1))
print(type(m))

name = "hhh"
name_type = type(name)
print(name)
print(name_type)

print(int(12.111))
print(int(12.55))
print(str(12.55))
print(float(12))
print(float(12.2))

"""
tips：
可以用变量存type()的结果，type(字面量/变量)
变量是无类型的，数据才有类型
有结果的语句（int(x)）都可以①用print输出②用变量存储
"""