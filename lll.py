import numpy as np
import matplotlib.pyplot as plt

# 建立一个从 -π 到 π 的 x 轴
x = np.linspace(-np.pi, np.pi, 100)

# 画一条正弦波，再画一条余弦波
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 4)) # 设定画布大小
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)', linestyle='--')
plt.title('My first step in GeoAI') # 标题
plt.legend() # 显示图例
plt.grid(True) # 显示网格
plt.show() # 弹出图表
