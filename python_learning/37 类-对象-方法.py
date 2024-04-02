# 在程序中设计表格，即设计类（class）
class Student:
    name = None    # 记录学生姓名
    gender = None  # 记录学生性别


# 在程序中打印表格，即创建对象（基于类创建对象）
stu_1 = Student()  # stu_1:即是变量也是对象（变量接收了对象）
stu_2 = Student()
# 在程序中填写表格，即对象属性赋值
stu_1.name = "小明"
stu_1.gender = "男"
stu_2.name = "小美"
stu_2.gender = "女"

print(stu_1.name)


# 类中可以定义成员变量（变量）和成员方法（方法）-（函数）
# 类【属性（数据），行为（函数）】
# 类的成员方法---self表示类对象自身的意思
print("---")


class Student:  # 类名开头大写
    name = None

    def say_hi(self, msg):
        print(f"hi,我是{self.name},{msg}")


stu = Student()
stu.name = "z"         # 对象.变量
print(stu.name)
stu.say_hi("hello")    # 对象.方法
