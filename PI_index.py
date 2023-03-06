# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PI_index
   Description :
   Author :       Jamerri
   date：          2022/10/31
-------------------------------------------------
   Change Activity:
                   2022/10/31:
-------------------------------------------------
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


"""定义参数"""
k_u = 2
k_p = 0.5
PI = []


def calculate_PI(concentration):
    """PI计算"""
    miu = np.mean(concentration)
    max_value = np.max(concentration)
    # max_no = concentration.index(max_value)
    pi = k_u * miu + k_p * max_value
    return pi


for i in range(10):
    """随机生成弄浓度数据"""
    concentration_value = np.random.randint(10, 40, size=[1, 60])
    PI.append(calculate_PI(concentration_value))

for i in range(10):
    """随机生成弄浓度数据"""
    concentration_value = np.random.randint(20, 80, size=[1, 60])
    PI.append(calculate_PI(concentration_value))

for i in range(10):
    """随机生成弄浓度数据"""
    concentration_value = np.random.randint(30, 120, size=[1, 60])
    PI.append(calculate_PI(concentration_value))

for i in range(10):
    """随机生成弄浓度数据"""
    concentration_value = np.random.randint(40, 160, size=[1, 60])
    PI.append(calculate_PI(concentration_value))

for i in range(10):
    """随机生成弄浓度数据"""
    concentration_value = np.random.randint(50, 200, size=[1, 60])
    PI.append(calculate_PI(concentration_value))

print(PI)

# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=12)

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

x = np.arange(0, 50)
fig, ax = plt.subplots()

ax.spines['top'].set_visible(False)  # 隐藏上端脊梁
ax.spines['right'].set_visible(False)  # 隐藏上端脊梁

# 设置线条参数
l1, = ax.plot(x, PI, marker='s', markersize=3, color='k', linewidth='1', linestyle='-', clip_on=False)

# 设置图例 bbox_to_anchor图例的位置 ncol设置列数 frameon设置边框
plt.legend(handles=[l1], labels=['Sensor 0'], bbox_to_anchor=(0.78, 1.1), loc=2, frameon=False)

# 设置坐标轴范围
plt.xlim(0, 50)
ax.set_ylim(0, 500)

ax.set_xlabel('No.', fontsize=12)
ax.set_ylabel('Proximity Index', fontsize=12, color='k')

# 设置X轴主刻度
axxmajorLocator = MultipleLocator(10)
ax.xaxis.set_major_locator(axxmajorLocator)

# 设置Y轴主刻度
axymajorLocator = MultipleLocator(50)
ax.yaxis.set_major_locator(axymajorLocator)

# 保存图片
plt.rcParams['figure.figsize'] = (8.0, 6.0)  # 设置figure_size尺寸
plt.savefig('pi_test.tif', bbox_inches='tight', dpi=600)
plt.show()
