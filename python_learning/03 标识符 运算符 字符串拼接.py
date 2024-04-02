"""
标识符（变量名，类名，方法名）命名规则
1.可以用英文、中文（不推荐）、数字、下划线
2.数字不能用于开头
3.大小写敏感
4.不可以用关键字
所以用全小写字母+（_）命名法，要做到
1.见名知意
2.下划线分隔法
3.全英文小写

运算符包括 + - * /,
//(整除) %(取余) **(指数)
"""
# 标识符
first_num = 1
# 运算符
print(9.0//2)
print(9//2.0)
print(9//2)
print(9 % 2)
print(2**4)
# \(转义符)
name = '\'d\''
print(name)
num = "'3'"
print(num)
# 字符串拼接（+ ，）
# （不同）字符串拼接+号没空格，逗号有空格
name = "wo"
print("我是"+name)
print("我是", name)
# 占位拼接%s(即格式化)
print("我今年%s岁，身高175" % 20)
age = 20
tall = 175
print("我今年%s岁，身高%s" % (age, tall))
# 占位好修改
# 格式化精度的控制
num_1 = 11.354
print("数字是%f" % num_1)
print("数字是%.2f" % num_1)
print("数字是%7.2f" % num_1)
# 主流格式化方式f{}：原封不动的放进去    （主流）
name = "邹邹"
age = 13
tall = 175.2
print(f"名字是{name}，年龄是{age}，身高是{tall}")
# 表达式如(1+1),type("周周")：
# 表达式是一条具有明确执行结果的代码语句,可以和前面变量一样进行格式化
print(f"字符串在python中的类型是{type("字符串")}")

# 作业
name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))

"""
字面量（3，4.3）  字面量包括数字、字符串、元组、列表、字典等
变量（x，y）
“+”能实现字符串变量或字符串字面量之间的拼接 （不用）
“%s”的%表示我要占位（即格式化），s表示将变量/字面量变为字符串放入占位处
%s转字符串 %d转整数 %f转浮点数
%m.n；m控制宽度 n控制精度（四舍五入）四舍五入所以会失真
表达式【（1+1），type("f")】可以直接格式化
"""