"""
异常捕获 try except
讲解：
try：包裹可能出错的代码。
except：捕获特定异常，避免程序崩溃。永远不要裸写 except:，应指定异常类型。
else：try 成功时执行。
finally：无论是否异常都执行（常用于资源清理）。

try-catch-finally 类比Java
"""
import json

# 示例代码
ex_json= '{"name": "Alice", "age": }'  #错误示例
try:
    data=json.loads(ex_json)
    name_ = ex_json["name"]
except json.decoder.JSONDecodeError as e:
    print(f"Json解析失败: {e}")
except KeyError as e:
    print("Json key error: {e}")
except Exception as e:
    print("Json error: {e}")
else:
    print(f"解析成功: {name_}")
finally:
    print("处理完成，释放资源")
