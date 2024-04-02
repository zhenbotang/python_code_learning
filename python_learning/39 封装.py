# 将现实世界事物在类中描述为属性和方法，即为封装
# 类中不公开的变量或方法可以定义为：私有成员变量和私有成员方法，类对象不能访问私有成员，类中其他成员可以访问私有成员
# 语法：在变量/方法前面加两个下划线（__）


# 定义一个手机的类，内含私有成员变量和私有成员方法
class Phone:
    id = None
    producer = None
    __current_voltage = 33

    def open_5g(self):  # 该函数并没有使用self相关的变量，因此可以把此函数设为静态方法即可
        print("5G已经打开")

    def __CPU_stop(self):  # 函数名要小写
        print("CPU已经停止工作")


iphone = Phone()
print(iphone.id)
print(iphone.producer)
# print(iphone.__current_voltage)

iphone.open_5g()
# iphone.__cpu_stop()

# 私有成员和方法可以被类中自己的方法调用
print("---")


class Phone:
    __current_voltage = 33

    def __CPU_stop(self):
        print("CPU已经停止工作")

    def open_5g(self):
        if self.__current_voltage > 33:  # 内部调用方法也要加self
            print("5G已经打开")
        else:
            self.__CPU_stop()


iphone = Phone()
iphone.open_5g()

print("---")


# 作业：设计带有私有成员的手机
class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:  # if self.__is_5g_enable == True:  # 判断是否等于： ==
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


iphone = Phone()
iphone.call_by_5g()
