# for “轮询”
# for 变量 in 被处理的数据（序列）
name = "123"
for x in name:
    print(x)
num = 123
for x in name:
    print(x)

# 作业
# 数一数有几个a
name = "itheima is a brand of itcast"
num = 0   # 原因是因为一个页面当中出现了两个相同的函数或者类(变量?)
# a = "a"
for x in name:
    if x == "a":  # "="是赋值 "=="才是比较
        num += 1
print(num)
