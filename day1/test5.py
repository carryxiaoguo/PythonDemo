# 函数讲解
"""
定义：使用 def 关键字。
参数类型：位置参数、默认参数、*args（接收多余位置参数为元组）、**kwargs（接收多余关键字参数为字典）。
返回值：使用 return，可返回多个值（自动打包为 tuple）。无 return 则返回 None。
"""
def greet(name,str = "hi",*tuple,**dict):
    """演示各种参数类型"""
    result = f"Hello,{name},{str}"
    for msg in tuple:
        result += f" {msg}"
    if dict.get("uppercase") :
         result = result.upper()
    return result
msg = greet("Bob","你好","abc",uppercase=True)
print(msg)

# 多返回值
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # return a // b,a % b

quotient, remainder = divide(17, 5)
print(f"商={quotient}, 余={remainder}")  # 商=3, 余=2