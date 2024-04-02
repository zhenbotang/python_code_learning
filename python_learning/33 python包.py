# python文件 + __init__.py的文件夹就是python包
# 调包语法：import 包名.模块名 ； 包名.模块名.方法名

# 调包方法1
import my_package.my_module
a = my_package.my_module.text(1, 2)
print(a)
# 调包方法2
from my_package import my_module
b = my_module.text(2, 3)
print(b)
# 调包方法3
from my_package.my_module import text
c = text(3, 4)
print(c)

# __init__.py 中可以写__all__ = [模块名]来控制import*

# 安装第三方包
# 方法：在命令提示符中输入：pip install 包名称（即可以通过网络快速安装第三方包）
# 加快安装速度：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
# 包导入到哪个解释器，哪个解释器里面才能用这个包
