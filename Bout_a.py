# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Bout_a
   Description :
   Author :       Jamerri
   date：          2022/10/31
-------------------------------------------------
   Change Activity:
                   2022/10/31:
-------------------------------------------------
"""


import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


"""定义参数"""
sigma_smooth: float = 0.3  # sigma值
time_half = 0.4  # 时间半衰期
time_step = 0.1  # 时间步长

Bout_amplitude = []


def calculate_Bout(concentration):
    """Bout计算"""
    origin_concentration = []
    smooth_concentration = []
    y_concentration = []
    for num in range(len(concentration)):
        origin_concentration.append(concentration[num])
    for num_x in range(len(origin_concentration)):
        s_concentration = origin_concentration[num_x] * math.exp((-1 * 1) / (2 * sigma_smooth * sigma_smooth)) / (sigma_smooth * math.sqrt(2 * math.pi))
        smooth_concentration.append(s_concentration)
    x_concentration = np.diff(smooth_concentration)
    x_concentration = x_concentration.tolist()
    x_concentration.insert(0, 0.0)
    y_concentration.insert(0, 0.0)
    alfa = math.exp(math.log10(1 / (2 * time_half * time_step))) - 1
    for num_y in range(1, 60):
        if num_y == 1:
            y_concentration.append(
                (1 - alfa) * y_concentration[0] + alfa * (x_concentration[num_y] - x_concentration[0]))
        else:
            y_concentration.append(
                (1 - alfa) * y_concentration[num_y - 1] + alfa * (x_concentration[num_y] - x_concentration[num_y - 1]))
    y_derivative = np.diff(y_concentration)
    y_derivative = y_derivative.tolist()
    y_cc = np.array(y_derivative)
    y_derivative_min = np.min(y_cc)
    y_derivative_max = np.max(y_cc)
    y_derivative_amplitude = y_derivative_max - y_derivative_min
    return y_derivative_amplitude


for i in range(10):
    concentration_value = []
    """随机生成弄浓度数据"""
    for j in range(60):
        concentration_value.append(np.random.randint(10, 40))
    Bout_amplitude.append(calculate_Bout(concentration_value))

for i in range(10):
    concentration_value = []
    """随机生成弄浓度数据"""
    for j in range(60):
        concentration_value.append(np.random.randint(40, 80))
    Bout_amplitude.append(calculate_Bout(concentration_value))

for i in range(10):
    concentration_value = []
    """随机生成弄浓度数据"""
    for j in range(60):
        concentration_value.append(np.random.randint(80, 120))
    Bout_amplitude.append(calculate_Bout(concentration_value))

for i in range(10):
    concentration_value = []
    """随机生成弄浓度数据"""
    for j in range(60):
        concentration_value.append(np.random.randint(120, 160))
    Bout_amplitude.append(calculate_Bout(concentration_value))

for i in range(10):
    concentration_value = []
    """随机生成弄浓度数据"""
    for j in range(60):
        concentration_value.append(np.random.randint(160, 200))
    Bout_amplitude.append(calculate_Bout(concentration_value))

print(Bout_amplitude)


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
l1, = ax.plot(x, Bout_amplitude, marker='s', markersize=3, color='k', linewidth='1', linestyle='-', clip_on=False)

# 设置图例 bbox_to_anchor图例的位置 ncol设置列数 frameon设置边框
plt.legend(handles=[l1], labels=['Sensor 0'], bbox_to_anchor=(0.78, 1.1), loc=2, frameon=False)

# 设置坐标轴范围
plt.xlim(0, 50)
ax.set_ylim(-1, 30)

ax.set_xlabel('No.', fontsize=12)
ax.set_ylabel('Bout number', fontsize=12, color='k')

# 设置X轴主刻度
axxmajorLocator = MultipleLocator(10)
ax.xaxis.set_major_locator(axxmajorLocator)

# 设置Y轴主刻度
axymajorLocator = MultipleLocator(5)
ax.yaxis.set_major_locator(axymajorLocator)

# 保存图片
plt.rcParams['figure.figsize'] = (8.0, 6.0)  # 设置figure_size尺寸
plt.savefig('Bout_test.tif', bbox_inches='tight', dpi=600)
plt.show()