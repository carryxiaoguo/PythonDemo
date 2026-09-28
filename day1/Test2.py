# ==========模块与包 导入方式 ==========
from datetime import datetime #按需导入
import math
import json as j  # as 起别名



math_sqrt = math.sqrt(16)
print(math_sqrt)
now= datetime.now()
data = j.dumps({"key": "value"})
# ========== 自定义模块 ==========
# 假设你创建了 utils.py，内容为: def helper(): print("help")
# 在同一目录下可以这样导入:
# from utils import helper
# helper()

# ========== 常用标准库速查 ==========
# os        → 文件/目录操作、环境变量
# sys       → 命令行参数、解释器信息
# json      → JSON序列化/反序列化
# random    → 随机数生成
# re        → 正则表达式
# collections → Counter, defaultdict, deque 等高级数据结构