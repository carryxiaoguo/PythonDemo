"""
json 数据解析
讲解：
json.loads(s)：JSON字符串 → Python对象（str→dict/list）。
json.dumps(obj)：Python对象 → JSON字符串。
json.load(fp) / json.dump(obj, fp)：文件读写版本。
关键参数：ensure_ascii=False（中文不转义）、indent=2（格式化输出）。

"""
import json
from email.header import UTF8
from encodings import utf_8
from textwrap import indent

# 字符串<->python对象
json_str = '{"name":"Amy","age":31,"scores":[90,85]}'
json_obj = json.loads(json_str)
print(json_obj['name'])
# 转python
#输出设置
dumps = json.dumps(
    json_obj,
    ensure_ascii=False,  # 保留中文
    indent=2 # 美化输出 占位符+竖向输出
)
print(dumps)
# === 文件读写 ===
with open("data.json","w",encoding="utf-8") as f:
    json.dump(json_obj,f,ensure_ascii=False,indent=2)
with open("data.json","r",encoding="utf-8") as f: # encoding must string,On the contrary type error
    loads = json.load(f)
    print(loads)