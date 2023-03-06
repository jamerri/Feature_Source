# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     draw_20221208
   Description :
   Author :       Jamerri
   date：          2022/12/8
-------------------------------------------------
   Change Activity:
                   2022/12/8:
-------------------------------------------------
"""


import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


file_path = './data/颗粒物-固定传感器采样数据-20221126/Mean_data_1.txt'

'''处理原始数据'''
# with as 操作已经打开的文件对象，无论期间是否抛出异常，都能保证with as语句执行完毕后自动关闭已经打开的文件。
with open(file_path, 'r', encoding='utf-8') as file_object:
    raw_data = file_object.readlines()[:]
for i in range(len(raw_data)):
    data = raw_data[i].strip('\n').split(' ')
    for j in range(len(data)):
        data[j] = float(data[j])
    raw_data[i] = data
np.set_printoptions(suppress=True)
raw_data = np.array(raw_data)
print(raw_data)

value_1 = raw_data[:, 0]
value_2 = raw_data[:, 1]
value_3 = raw_data[:, 2]
value_4 = raw_data[:, 3]
value_5 = raw_data[:, 4]
value_6 = raw_data[:, 5]

print(len(value_1))

# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=12)

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

x = np.arange(0, 50)
fig, ax = plt.subplots()

ax.spines['top'].set_visible(False)  # 隐藏上端脊梁
ax.spines['right'].set_visible(False)  # 隐藏上端脊梁

'''颜色bar调整'''
color_1 = '#ff0000'  # 红色
color_2 = '#00ff00'  # 绿色
color_3 = '#0000CD'  # 蓝色
color_4 = '#ffff00'  # 黄色
color_5 = '#00bfff'  # 深天蓝
color_6 = '#4169E1'  # 宝蓝色
color_7 = '#1E90FF'  # 闪蓝色
color_8 = '#6495ED'  # 矢车菊色
color_9 = '#00FFFF'  # 青色
color_10 = '#FF9900'  # 橙色
color_11 = '#ff8C00'  # 橙红色
color_12 = '#87CEFA'  # 浅天蓝
color_13 = '#ffff66'

# 设置线条参数
l1, = ax.plot(x, value_1, marker='s', markersize=3, color='#ff0000', linewidth='1', linestyle='-', clip_on=False)
l2, = ax.plot(x, value_2, marker='s', markersize=3, color='#00ff00', linewidth='1', linestyle='-', clip_on=False)
# l3, = ax.plot(x, value_3, marker='s', markersize=3, color='#0000CD', linewidth='1', linestyle='-', clip_on=False)
# l4, = ax.plot(x, value_4, marker='s', markersize=3, color='#00bfff', linewidth='1', linestyle='-', clip_on=False)
l5, = ax.plot(x, value_5, marker='s', markersize=3, color='#6495ED', linewidth='1', linestyle='-', clip_on=False)
# l6, = ax.plot(x, value_6, marker='s', markersize=3, color='#00FFFF', linewidth='1', linestyle='-', clip_on=False)

# # 设置图例 bbox_to_anchor图例的位置 ncol设置列数 frameon设置边框
# plt.legend(handles=[l1, l2, l3, l4, l5, l6], labels=['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6'], bbox_to_anchor=(0.78, 1.1), loc=2, frameon=False)

# 设置坐标轴范围
plt.xlim(0, 50)
# ax.set_ylim(-1, 30)

ax.set_xlabel('No.', fontsize=12)
ax.set_ylabel('MSC value', fontsize=12, color='k')

# 设置X轴主刻度
axxmajorLocator = MultipleLocator(10)
ax.xaxis.set_major_locator(axxmajorLocator)

# # 设置Y轴主刻度
# axymajorLocator = MultipleLocator(5)
# ax.yaxis.set_major_locator(axymajorLocator)

# 保存图片
plt.rcParams['figure.figsize'] = (8.0, 6.0)  # 设置figure_size尺寸
# plt.savefig('./data/颗粒物-固定传感器采样数据-20221126/MSC.tif', bbox_inches='tight', dpi=600)
plt.show()
