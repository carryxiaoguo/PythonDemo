"""
asyncio 异步基础（重点）
讲解：
⚠️ 核心思想：
    异步不是多线程！它是单线程协作式并发。当一个任务遇到 I/O 等待时，主动让出控制权给事件循环，
    去执行其他任务。适用于 I/O 密集型（网络请求、文件读写、数据库），不适用于 CPU 密集型计算。
async def：定义协程函数（coroutine），调用它不会执行，而是返回协程对象。
await：挂起当前协程，等待异步操作完成，同时让出控制权。只能在 async def 中使用。
asyncio.run()：程序入口，启动事件循环。
asyncio.gather()：并发执行多个协程（区别于顺序 await）。
asyncio.sleep()：模拟异步 I/O 等待（time.sleep 会阻塞整个事件循环，绝对禁止在异步代码中使用）。

1. I/O 密集型
定义：程序大部分时间在 "等"——等网络响应、等磁盘读写、等数据库查询、等用户输入。CPU 实际干活的时间很少，大量时间处于空闲等待状态。
典型场景举例：
爬虫同时请求 100 个网页（每个请求要等服务器返回 200ms）
批量上传/下载文件到 OSS/S3
Web API 服务处理大量用户的 HTTP 请求（每次都要查数据库）
读取多个大日志文件并逐行解析
向消息队列（RabbitMQ/Kafka）批量发送消息
调用第三方 AI 接口、支付接口、短信接口

这两个概念是理解 asyncio（以及所有并发编程）的核心前提。我用最直白的例子解释：
1. I/O 密集型
定义：程序大部分时间在 "等"——等网络响应、等磁盘读写、等数据库查询、等用户输入。CPU 实际干活的时间很少，大量时间处于空闲等待状态。
典型场景举例：
爬虫同时请求 100 个网页（每个请求要等服务器返回 200ms）
批量上传/下载文件到 OSS/S3
Web API 服务处理大量用户的 HTTP 请求（每次都要查数据库）
读取多个大日志文件并逐行解析
向消息队列（RabbitMQ/Kafka）批量发送消息
调用第三方 AI 接口、支付接口、短信接口
为什么适合 asyncio？
因为 await 可以在"等待"时把 CPU 让给其他任务。100 个请求不用串行等 20 秒，而是几乎同时发出，总耗时 ≈ 单次请求时间。
CPU 利用率低，但吞吐量极高。
2. CPU 密集型
定义：程序大部分时间在 "算"——CPU 持续满负荷运算，几乎没有等待 I/O 的间隙。瓶颈在 CPU 算力本身，而不是外部资源。
典型场景举例：
表格
场景	具体例子
图像/视频处理	用 Pillow/OpenCV 对 1000 张图片做缩放、滤镜、人脸识别
数据加密/解密	AES/RSA 批量加密文件、生成哈希
科学计算	NumPy 矩阵运算、FFT 变换、物理模拟
机器学习推理	本地运行 PyTorch/TensorFlow 模型预测
压缩/解压	gzip/zstd 压缩大量数据
复杂算法	排序百万级数据、路径规划、密码暴力破解
JSON/XML 序列化	解析/生成超大 JSON 文件（纯 CPU 解析，非网络）
正则匹配	对海量文本执行复杂正则提取

"""



import asyncio
import time


# 正确的异步操作
async def fetch_data(name: str, delay: float) -> dict:
    print(f"[{time.strftime('%H:%M:&S')}]{name}")
    await asyncio.sleep(delay) #模拟网络IO，让出控制权
    print(f"[{time.strftime('%H:%M:%S')}] {name} 完成 ✓")
    return {"name":name,"delay":delay}
# 错误示范：time.sleep 会阻塞整个事件循环
# async def bad_fetch():
#     time.sleep(2)  # 绝对禁止！
async def main():
    start = time.time()
    #顺序执行中总耗时=各项耗时相加
    r1 = await fetch_data("A",2)
    r2 = await fetch_data("B",5)
    print(r1)
    print(r2)
    end = time.time()
    res = end - start
    res = round(res,2) #保留两位小数
    print(f"功耗时间:{res}")
if __name__ == "__main__":
    asyncio.run(main())
