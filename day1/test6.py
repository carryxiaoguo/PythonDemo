"""
面向对象：类、实例、初始化
讲解：
类 (Class)：蓝图/模板，使用 class 定义。
初始化 (__init__)：构造方法，创建实例时自动调用，用于绑定实例属性。
实例：类的具体对象，通过 ClassName() 创建。
self：代表实例本身，访问实例属性和方法必须通过 self。
"""
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._login_count = 0 # 私有属性

    def login(self): # 函数(User uer）
        self._login_count += 1
        return f"{self.name},第{self._login_count}登录"

    def info(self):
        return {"name": self.name, "age": self.age}
#创建示例
user = User("Amy", 19)
#调用方法
print(user.login())
print(user.info())
