# 类的继承：就是一个类继承一个或多个类的成员变量和成员方法
# （单继承）语法：class 类名（父类名）：
#          类的内容
# 子类与父类

class Phone:
    id = 303
    producer = "heima"

    def call_by_4g(self):
        print("正在使用4g通话中")


class Phone2024(Phone):
    face_id = "100010"

    def call_by_5g(self):
        print("2024新功能,使用5g通话中")


phone = Phone2024()
print(phone.id)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class Phone:
    id = 303
    producer = "heima"

    def call_by_4g(self):
        print("正在使用4g通话中")


class NFC:
    nfc_type = "第五代NFC"

    def read_card(self):
        print("读卡中")


class Remote_Control:
    id = "302"
    def control(self):
        print("远程遥控开启")


class NewPhone(Phone, NFC, Remote_Control):
    pass  # 只继承不添加新内容用pass（表示空）关键字


iphone = NewPhone()
print(iphone.producer)
print(iphone.nfc_type)
iphone.control()
print(iphone.id)  # 多父类中，如果有同名成员，那么默认以（从左到右的）继承顺序为优先级（先继承的保留）


# 复写（对父类的成员不满意可以进行复写），在子类中重新定义同名属性或方法即可
class Phone:
    id = 303
    producer = "heima"

    def call_by_4g(self):
        print("使用4g通话中")


class NewPhone(Phone):
    id = "304"

    def call_by_4g(self):
        print("正在使用4g通话中")


print("---")
phone = NewPhone()
print(phone.id)
phone.call_by_4g()

# 调用父类成员：父类名.成员变量/成员方法（self） 或 super（）.成员变量/成员方法（）
class Phone:
    id = 303
    producer = "heima"

    def call_by_4g(self):
        print("使用4g通话中")


class NewPhone(Phone):
    id = "304"

    def call_by_4g(self):
        print("加速中")
        print(f"父类的id是{Phone.id}")
        Phone.call_by_4g(self)
        super().call_by_4g()


print("---")
phone = NewPhone()
print(phone.id)
phone.call_by_4g()
