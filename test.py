"""GeoAI 环境测试脚本

用途：验证当前 Python 解释器能否正常工作，并检查 numpy / matplotlib 是否可用。
运行后会打印 "Hello GeoAI"，并生成一张正弦波图。
"""

import sys
from pathlib import Path

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# ---------- 1. 打印信息 ----------
print("Hello GeoAI")
print(f"Python     : {sys.version.split()[0]}")
print(f"解释器路径 : {sys.executable}")
print(f"numpy      : {np.__version__}")
print(f"matplotlib : {matplotlib.__version__}")

# ---------- 2. 生成正弦波数据 ----------
x = np.linspace(0, 2 * np.pi, 500)   # 0 ~ 2π，共 500 个点
y = np.sin(x)

# ---------- 3. 画图 ----------
plt.figure(figsize=(8, 4))
plt.plot(x, y, linewidth=2, label="sin(x)")
plt.title("Hello GeoAI - Sine Wave")
plt.xlabel("x (radian)")
plt.ylabel("sin(x)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# ---------- 4. 保存图片（保存在本脚本所在目录） ----------
out_file = Path(__file__).with_name("sine_wave.png")
plt.savefig(out_file, dpi=150)
print(f"图片已保存 : {out_file}")

# ---------- 5. 弹出窗口显示（用终端命令行运行时需要手动关闭窗口） ----------
plt.show()
