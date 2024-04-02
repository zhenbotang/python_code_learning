# 导包：from 包.模块 import 功能对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts

# 得到折线图对象
line = Line()  # line就是对象（折线图对象）
# 添加x轴y轴数据
line.add_xaxis(["中", "美", "韩"])
line.add_yaxis("GDP", [1, 2, 3])  # axis 轴
# 设置全局配置项(set_global_opts)
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),        # 图例
    toolbox_opts=ToolboxOpts(is_show=True),      # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True),  # 视觉映射
    tooltip_opts=TooltipOpts(is_show=True),

)  # ctrl+p能显示可以输入的选项，可以在pyecharts.org学习



line.render()
# 会在右边文件里面生成html网页文件
