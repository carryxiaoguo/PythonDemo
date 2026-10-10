import functools
import time

# ========== 基础装饰器模板  此处复杂 ==========
def timer(func):
    """测量函数执行时间的装饰器"""
    @functools.wraps(func)  # ⚠️ 关键！保留原函数的 __name__、__doc__ 等元信息
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)   # 调用原始函数
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] 耗时: {elapsed:.4f}s")
        return result                     # ⚠️ 别忘了返回原函数的返回值
    return wrapper

@timer                    # 等价于 slow_func = timer(slow_func)
def slow_func(n: int):
    """一个模拟耗时操作的函数"""
    time.sleep(n)
    return n * 2

print(slow_func(1))       # [slow_func] 耗时: 1.0012s \n 2
print(slow_func.__name__) # slow_func ← 因为用了 @wraps，名字没被覆盖


# ========== 带参数的装饰器（三层嵌套）==========
def retry(max_attempts: int = 3, delay: float = 1.0):
    """带参数的装饰器需要再多一层嵌套"""
    def decorator(func):           # 第二层：接收被装饰的函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # 第三层：实际包装逻辑
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{attempt}次失败: {e}")
                    if attempt == max_attempts:
                        raise           # 最后一次仍失败，抛出异常
                    time.sleep(delay)
        return wrapper
    return decorator                 # 第一层：接收装饰器参数，返回真正的装饰器

@retry(max_attempts=3, delay=0.5)   # 注意：带参数时必须加括号
def unstable_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("网络超时")
    return {"status": "ok"}  