# json数据格式：用于不同编程语言之间传递数据（类似全球通用语英语）
# json要么是字典要么是列表（里面必须嵌套字典），并且数据都是字符串
# 将python转为json：data = json.dumps(data)
# 将json转为python：data = json.loads(data)
import json
# 将python转为json
data = [{"name": "小明", "age": 1}, {"name": "小美", "age": 2}, {"name": "小侯", "age": 3}]
print(data, type(data))
data = json.dumps(data, ensure_ascii=False)  # 转化为json时有中文需要转化要加上（ensure_ascii=False)
print(data, type(data))                      # ensure_ascii=False表示不用ascii来转化而是直接输出

print("---")
data2 = {"name": "小明", "age": 1}
print(data2, type(data2))
data2 = json.dumps(data2, ensure_ascii=False)
print(data2, type(data2))

# 将json转为python
print("---")
data3 = '{"name": "小明", "age": 1}'  # 要加引号(里面是双引号，所以外面单引号)
data3 = json.loads(data3)
print(data3, type(data3))
