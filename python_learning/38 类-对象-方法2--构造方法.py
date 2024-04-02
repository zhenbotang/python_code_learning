# ①基于类创建对象，面向对象编程
# 类是程序中的“设计图纸”，对象是基于图纸生产的具体实体
# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 300)  # 3000毫秒即3秒


# 构建具体闹钟对象1
clock1 = Clock()
clock1.id = "001"
clock1.price = "100"

# 让对象1工作
print(f"闹钟编号为{clock1.id},价格为{clock1.price}")
clock1.ring()


# ②构造方法：快速对成员变量赋值
# 构造方法和普通的成员方法都要加self
class Student:
    def __init__(self, name, age, tel):  # 即构造方法，构造方法不同于普通方法，构造方法会自动执行
        self.name = name  # 定义+赋值
        self.age = age
        self.tel = tel    # 在（构造）方法内定义成员变量，需要使用self关键字
        print("Student类创建了一个类对象")


student1 = Student("小明", 11, 661)
print(f"学生1的姓名为{student1.name}，年龄为{student1.age}，电话为{student1.tel}")


# 构造方法的作业
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


count = 0  # 可以直接用（i+1）
for i in range(10):
    student = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
    count += 1
    print(f"学生{count}信息录入完成，信息为【姓名：{student.name},年龄：{student.age},地址：{student.address}】")


"""
b站大佬的答案
"""
# 练习：学生信息录入
# 构造类Student
class Student:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add


# 创建空字典，存放学生信息
stu_dict = {}

# for循环录入信息
for i in range(1):
    print(f"当前录入第{i + 1}位学生信息，总共需要录入10位学生信息。")
    stu = Student(input("请输入学生姓名："),
                  input("请输入学生年龄："),
                  input("请输入学生地址：")
                  )
    stu_dict[f"学生{i+1}"] = {}    # 此步为嵌套字典的创建，key是stu_dict[f"学生{i+1}"]，value是{}
    stu_dict[f"学生{i+1}"]["姓名"] = stu.name
    stu_dict[f"学生{i+1}"]["年龄"] = stu.age
    stu_dict[f"学生{i+1}"]["地址"] = stu.add

    print(f"学生{i + 1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.add}】")

print("所有学生信息录入完毕。")

print(stu_dict)

