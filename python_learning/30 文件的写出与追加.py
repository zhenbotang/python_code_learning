# 文件的写入
# open（用w）写入时若文件不存在会创建文件，若文件存在会清除原有内容再写入
f = open("D:/text3.txt", "w", encoding="UTF-8")
f.write("123")
f.flush()  # 前面写入到了内存中，未进入硬盘，flush刷新后进入硬盘
f.close()  # close内置了flush的功能

# 文件的追加
# a模式：文件不存在会创建，存在会追加
f = open("D:/text3.txt", "a", encoding="UTF-8")
f.write("123")

# 作业
f = open("D:/bill.txt", "r", encoding="UTF-8")
g = open("D:/bill2.txt", "w", encoding="UTF-8")
# content = f.read()
# print(content)
# f.close()
# f = open("D:/bill.txt", "r", encoding="UTF-8")
for line in f:
    line = line.strip()  # strip字符串的方法是不改变原字符串而是生成新字符串
    if line.count("测试") == 1:
        continue
    else:
        g.write(line)
        g.write("\n")
    print(line, type(line))
f.close()
g.close()
