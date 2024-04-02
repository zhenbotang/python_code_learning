# 函数进阶
# 1 函数多返回值
def return_num():
    return 1, 2
a, b = return_num()
print(a, b)

# 2 函数的多种参数使用形式
# ①位置参数，关键字参数
def infer(name, age, gender):
    print(f"名字:{name},年龄:{age},性别:{gender}")
infer("a",age=2,gender="nan")  # 位置参数必须在关键字参数前面，关键字参数可以无序

# ②缺省参数（默认参数）不传参就使用默认值，默认值需要写在最后
def infer(name, age, gender="nan"):
    print(f"名字:{name},年龄:{age},性别:{gender}")
infer("a", age=2)

# ③不定长参数（传入参数数量不定）
# 位置传递，以元组输出
def a(*args):
    print(args)
a(1,2,3)

# 关键字传递，以字典输出
def b(**kwargs):
    print(kwargs)
b(age = 1, name = "xiao")


# 3 匿名函数
# ①函数作为参数传递
def func1(func2):
    result = func2(1, 2) + 1
    print(f"结果是{result}，func2类型是{type(func2)}")
def func2(x, y):
    return x + y

func1(func2)
# 普通函数传入数据（可以更改传入数据），此函数传入代码的执行逻辑（可以更改传入函数）
# func1要求传入函数，处理1，2
# ②lambda匿名函数 （只能临时使用一次）
# 匿名函数：lambda 传入参数：函数体（一行代码）
print()
def func1(compute):
    result = compute(1, 2) + 1
    print(f"结果是{result}，func2类型是{type(func1)}")


func1(lambda x, y: x + y)

# func1() takes 1 positional argument but 2 were given
# func1（）接受1个位置参数，但给定了2个
