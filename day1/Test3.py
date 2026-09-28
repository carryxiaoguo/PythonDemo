# ==================学习类与继承==================
class Animal:
    # 类变量：所有实例共享，通常用于常量或计数器
    kingdom = "Animal"

    def __init__(self, name: str, age: int):
        """"构造方法:创建实例独有"""
        self.name = name  # 示例变量:每个示例独有
        self.age = age
        self._internal = "私有约定"  # 单下划线：私有约定，不强制
        self.__secret = "名称改写"  # 双下划线：触发名称改写

    def speak(self) -> str:
        """普通实例方法：第一个参数必须是 self,返回值是str"""
        return f"{self.name} makes a sound"

    @classmethod
    def from_str(cls, s: str):
        """类方法：第一个参数是类本身(cls)，常用作替代构造函数  类比Java的静态工厂 public static Animal fromStr(String s){}"""
        name, age = s.split(",")
        return cls(name.strip(), int(age.strip()))  # cls() 等价于 Animal()

    @staticmethod
    def is_valid_age(age: int) -> bool:
        """静态方法：不需要 self 或 cls，本质是放在类命名空间下的普通函数
        @staticmethod	static 工具方法	命名空间归属，纯函数
        """
        return age >= 18

    @property
    def info(self) -> str:
        """
        属性装饰器：让方法可以像属性一样访问（无需加括号）-> Java 的 Getter 方法 + Lombok @Getter
         如果 @property 还定义了 setter，则对应 Java 的 getter/setter
         """
        return f"姓名:{self.name},{self.age}岁"

    def __str__(self) -> str:
        """魔法方法：print(obj) 或 str(obj) 时调用"""
        return f"Animal({self.name})"

    def __repr__(self) -> str:
        """魔法方法：调试/交互式环境中显示，应返回可重建对象的字符串"""
        return f"Animal(name='{self.name}', age={self.age})"


# ========== 继承与多态 ==========
class Dog(Animal):
    """"继承Animal"""

    def __init__(self, name: str, age: int, nikc: str):
        # ⚠️ 必须显式调用父类构造方法，否则父类的 __init__ 不会执行
        super().__init__(name, age)
        # 子类特有属性
        self.nikc = nikc

    # 重写speak方法
    def speak(self) -> str:
        return f"{self.name} hello，world"

    # 新增子类特有方法
    def sing(self, sing: str) -> str:
        return f"{self.name},唱{sing}!"


# ====================演示==========================
dog = Dog("旺财", 18, "Larry")
print(dog.speak())
print(dog.sing("Larry"))
print(dog.info)
print(dog.is_valid_age(18))
Dog.from_str("Amy", 5)  #
