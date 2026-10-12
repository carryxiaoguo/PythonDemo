"""
requests 网络请求
讲解：
安装：pip install requests
核心方法：get() / post() 最常用。
响应对象：.status_code 状态码、.json() 解析JSON、.text 文本内容。
超时：务必设置 timeout，防止请求永久阻塞。
"""
import requests

#GET请求
req = requests.get(
    "http://httpbin.org/get",
    params={"hello": "world"}, #URL查询参数
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=5
)
print(f"状态码:{req.status_code}")
json = req.json()
print(f"响应数据:{json['args']}")
# POST请求
post_resp = requests.post(
    "http://httpbin.org/post",
    json={"key1": "value1"},  # 自动序列化为JSON并设置Content-Type
    timeout=5
)
print(post_resp.json()["json"])
















