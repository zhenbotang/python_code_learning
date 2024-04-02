# 4种魔术方法,类的内置函数————# 不写__str__等魔术方法，输出对象（stu）就会是内存地址
# ①__str__，内置函数__str__定义了打印规则
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name:{self.name}, age:{self.age}"  # 通过__str__的魔术方法将类转为字符串，返回


stu = Student("周杰伦", 18)
print(stu, type(stu))
print(str(stu), type(str(stu)))

# ②__lt__:小于符号的比较
# 内置函数__lt__定义了比较规则


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student2("bob", 11)
stu2 = Student2("mike", 13)
print(stu1 < stu2)
print(stu1 > stu2)

# ③__le__:小于等于的比较，逻辑与__lt__一样


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age


stu1 = Student2("bob", 10)
stu2 = Student2("mike", 10)
print(stu1 <= stu2)
print(stu1 >= stu2)

# ④__eq__:等于的比较，逻辑与__lt__一样


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student2("bob", 10)
stu2 = Student2("mike", 10)
print(stu1 == stu2)
print(stu1 == stu2)
