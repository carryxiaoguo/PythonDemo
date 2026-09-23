# ============== 基本的输入输出 ============
# 输出语句
print("Hello World")
# 输入语句
# ①
#day1 = input("这是第一天")
# ② 须在控制台输入 才会打印 从内到外循环
# print(input("这是day1"))
# ================= 合法标识符 =================
"""
age = 25                # 普通变量名，最常见
user_name = "Alice"     # 用下划线连接单词，清晰易读
_total = 100            # 下划线开头通常表示“内部使用”或“私有”
MAX_SIZE = 1024         # 全大写通常表示“常量”（固定不变的值）
calculate_area()        # 函数名，动词+名词
StudentInfo             # 类名，首字母大写（驼峰命名法）
__private_var           # 双下划线开头，有特殊含义
"""
# ================= 赋值语句 =================
int_type = 12 #整型
float_type = 3.14 #浮点型
bool_type = True # 布尔型
str_type ="1000" # 字符串
print(type(str_type)) #查看数据类型 type关键字
# ================= 类型转换 ============
str_type = int(str_type) # 字符串->整型
print(type(str_type))
print(str_type)
# ==================== 字符串拼接与格式化 ========================
str1 = "hello"
str2 = "world"
result = str1 +" "+ str2 #字符串拼接
print(result) #打印
# f-string 格式化
msg =f"{str1},{str2}! Age:{int_type}"  # 花括号内可直接放变量/表达式
print(msg)
# ===========常用字符串方法================
text = " hello,python "
print(text.split()) #去除首尾空白
print(text.upper()) # 全部大写
print(text.lower()) # 全部小写
print(text.replace("python","Java")) # 替换子串
print("python" in text)  #True 判断子串是否还在
print(text.split(",")) # 逗号分隔开
print(len(text)) #获取字符串长度
print(text)
# ========== 列表 list（有序、可变、可重复）==========
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # 末尾添加元素
fruits.remove("orange") # 删除元素
fruits.insert(1, "avocado") # 在索引1处添加元素
popped = fruits.pop() #弹出最后一个元素
print(popped)
fruits_ = fruits[0:2] # 切片：取索引0到1的元素（不含2）
print(fruits_) #打印元素0和元素1
num_list = [2,3,1,4] # 新的数字列表，更直观看清排序
num_list.sort() #排序 res = num_list.sort() => none
sorted_list = sorted(num_list) # 有返回值且排序好的列表 复印一份再排"，安全但费内存
print(num_list)
print(len(fruits)) #获取列表长度
print(fruits)
# ========== 元组 tuple（有序、不可变、可重复）==========
point = (1,3,5,5,2)
# point[0] = 5 报错元组不可修改
new_tuple = (1,) #单元素必须结尾加逗号
print(point)
print(new_tuple)
# ========== 字典 dict（键值对、键唯一、无序）类比Java的Map==========
person = {          # 键必须是不可变类型（str/int/tuple）
    "name" : "Alice",
    "age" : 25,
    "city" : "San Francisco",
    "skill" :["Java","Python"]      #可以嵌套列表
}
person["email"] = "a@b.com" #添加K V
del person["city"] #删除指定K，V
name = person.get("name","Amy") # 安全获取，键不存在时返回默认值 ,意思获取name为Amy的字段
get_Keys = person.keys() #获取所有键
get_Values = person.values() #获取所有值
# ========== 集合 set（无序、不重复）==========
nums = {1,3,3,4,4,2,5} # 自动去重 1 3 4 2 5
nums.add(6)     #添加元素
nums.discard(5) # 删除元素（不存在也不报错）
a = {1,2,3}
b = {2,3,4}
print(a & b)                # 交集 → {2, 3}
print(a | b)                # 并集 → {1, 2, 3, 4}
print(a - b)                # 差集 → {1}
print(a ^ b)                # 补集 -> {1,4}
# ========== if-elif-else ==========
score = 89;
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
# 三元运算符  表达式1 判断体 表达式2
res = "及格" if score >= 60 else "不及格" # Java ：判断体 : 表达式1 ? 表达式2

# ========== for 循环 ==========
# 遍历列表
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "apple":
        print("你选择了苹果")
# range() 生成数字序列
for i in range(1,10): #包头不包尾
    print(i)
for i in range(1, 10, 2):   # 从1到9，步长为2 → 1,3,5,7,9
    print(i)
# enumerate 同时获取索引和值
for idx, val in enumerate(["a", "b", "c"]):
    print(f"索引{idx}: {val}")
# ========== while 循环 ==========
count = 0
while count < 5:            # 条件为True时持续执行
    print(count)
    count += 1              # ⚠️ 别忘了更新条件，否则死循环

# ========== break 与 continue ==========
for n in range(10):
    if n == 3:
        continue            # 跳过本次循环，进入下一次
    if n == 7:
        break               # 彻底退出整个循环
    print(n)                # 输出: 0 1 2 4 5 6

# ========== 函数 基本定义 ==========
def greet(str_name,greeting = "world"):
    """这是文档字符串(docstring)，描述函数功能"""
    return f"{str_name} {greeting}!"
print(greet("hello")) # greeting参数使用默认
print(greet("hello","python")) #修改默认参数

# ========== 可变参数 ==========
def add(*args):         # *args 接收任意数量的位置参数，打包成元组
    return sum(args)

def info(**kwargs):     # **kwargs 接收任意关键字参数，打包成字典
    for k, v in kwargs.items():
        print(f"{k}: {v}")
print(add(1, 2, 3, 4, 5, 6))
info(name = "Amy",age = 25,city = "San Francisco")
# ========== Lambda 匿名函数 ==========
square = lambda x: x ** 2       # 等价于 def square(x): return x**2  表达式 lambda 参数 ：方法体 ，可有返回值
print(square(5))                # 25
# 常配合 sorted/map/filter 使用
words = ["appless", "banana", "cherry"]
sort_words = sorted(words,key=lambda word: len(word))
print(sort_words)
# ========== try-except 异常处理 ==========
try:
    num = int(input("请输入数字: "))
    result = 10 / num
except ValueError:              # 捕获特定异常：输入非数字
    print("输入无效，请输入数字")
except ZeroDivisionError:       # 捕获除零错误
    print("不能除以零")
except Exception as e:          # 捕获所有其他异常
    print(f"未知错误: {e}")
else:                           # 没有异常时才执行
    print(f"结果: {result}")
finally:                        # 无论是否异常都执行（常用于清理资源）
    print("执行完毕")

# ========== 文件读写 ==========
# 写入文件（with 语句自动关闭文件，防止资源泄漏）
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")         # \n 是换行符
    f.writelines(["第二行\n", "第三行\n"])  # 写入多行

# 读取文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 一次性读取全部内容
    # lines = f.readlines()     # 读取所有行为列表
    # line = f.readline()       # 逐行读取

# 追加模式："a"  二进制模式："rb"/"wb"
