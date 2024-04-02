# for的嵌套与while类似
# 100天每天送10朵玫瑰后表白
x = 0  # 提前定义内部变量方便使用
for x in range(100):
    print(f"第{x+1}天")
    for y in range(10):
        print("sending rose")
    print("i love you")
print(f"第{x+1}天，Confession successful")

# for语句实现99乘法表
for x in range(1, 10):
    for y in range(x):
        print(f"{y+1}*{x}={(y+1)*x}\t", end='')
    print()
