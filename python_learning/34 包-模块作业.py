# 自定义工具包的调用
import my_tool.str
import my_tool.file  # from my_tool import file
a = my_tool.str.str_reverse("name")
b = my_tool.str.substr("name is Bob", 4, 8)
print(a)
print(b)

my_tool.file.print_file_info("E:/text.txt")
my_tool.file.append_to_file("E:/text.txt", "追加测试")
