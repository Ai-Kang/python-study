# python注释
```text
单行注释：# 注释内容

'''
 我是行注释
'''

"""
 我是多行注释
"""
```
# 变量与常量
```text
# 定义变量
year = 2024
# 定义常量
PI = 3.1415926
# 判断类型 返回bool
print(isinstance(数据, int))
# 转int
int(x,[基数])
print(int(2.13))
print(int('10', 2))  # 二进制的10
float(x)
bool(x)
str(x)
```
# 数据类型
## int 整数
```python
# int 整数
a = 123
print(type(a))
a1 = -123
# 基础运算
print(a + a1)
print(a - a1)
print(a / a1)
print(a * a1)
```

## float 浮点数
```python
# float 浮点数
c = 1.23
print(type(c))
c1 = -1.23
# 基础运算
print(c + c1)
print(c - c1)
print(c * c1)
print(c / c1)
print(c % c1)

c2 = 3.1
c3 = 2.2
print(c2 + c3)  # 5.300000000000001
print(round(c2 + c3, 2))  # 四舍五入  5.3

import math
print(math.ceil(c2 + c3))  # 向上取整 6
print(math.floor(c2 + c3))  # 向下取整 5
```
# bool 布尔值
```python
# bool 布尔值  真True 假False
d = True
print(type(d))
```
## str 字符串
```python
# str 字符串
str1 = 'abc'
str2 = "dfg"
str3 = '''
        abc
        dfg
       '''
str4 = """
        abc
        dfg
       """
print(type(str3))
print(str1 * 2)  # 重复出现两次 abcabc
print(str1 + str2)  # abcdfg
print(str1[0])  # 索引从0开始 a
print(str1[0:3])  # 切片 abc 包左不包右
print(str1[0:3:2])  # 切片 ac 包左不包右,步长
```
## 序列
**序列是有序排列并且可以通过下标获取内容的列表，包括列表、range、元组和字符串**
## 序列通用函数
```pycon
len(item)       计算容器中元素的个数
del(item)       删除元素
max(item)       返回容器中最大值
min(item)       返回容器中最小值
item[0:10:2]    切片[开始索引:结束索引:步长]  左包又不包
enumerate(item)
for i,v in enumerate(item)
```
## 序列通用运算符
```pycon
+       [1,2] + [3,4]   结果  [1,2,3,4]
*       ['hi'] * 4      结果  ['hi','hi','hi','hi']
in      3 in (1,2,3,4)  结果  bool   判断元素是否存在
not in  3 in (1,2,3,4)  结果  bool   判断元素是否不存在
<       大小比较         结果  bool
<=      大小比较         结果  bool
==      大小比较         结果  bool
>       大小比较         结果  bool
>=      大小比较         结果  bool
```
### list 列表
```python
# list 列表
g = [1, 2, "a", "b"]
print(type(g))
h = list()
# 取出元素,支持切片
print(g[2])
# 添加一个元素
g.append([1, 2])
# 追加一个列表
g.extend([1, 2, 3])
# 插入元素
g.insert(2, "aaa")
# 根据索引删除元素
g.pop(3)
# 根据元素删除第一个元素
g.remove("b")
# 清空
g.clear()
```
### tuple 元组
```python
# tuple 元组，元素不允许改变
h = (1, "2", "a")
print(type(h))
```
### range
```pycon
# range函数,生成列表
print(type(range(0,6,1)))
```
### str 字符串
```pycon
# str 字符串
s1 = "hello worf"
print(s1 + " abc")
print(len(s1))
# 是否都小写
print(s1.islower())
# 是否都大写
print(s1.isupper())
# 计数
print(s1.count('o'))
# 去除前后空格
print(s1.strip())
# 分割字符串
print(s1.split(' '))
# 查找元素第一次出现的位置
print(s1.find(' '))
# 使用字符串连接数据
print('*'.join(['11','22','33','44']))
# 转换小写
print(s1.lower())
# 转换大写
print(s1.upper())
```
### dict字典
```python
# dict 字典 无序
d = {"name": "aikang", "age": 23}
print(type(d))
print(d["name"])
d["name"] = 'zp'
print(d["name"])
for k,v in d.items():
    print(k,v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
# 删除元素
d.pop("age")
print(d.get("name"))
# 从最后删除一个
d.popitem()
# 字典拼接
d.update({"to":"day"})
print(d)
# 清空
d.clear()
```
### set 集合
```python
# set 集合,不重复序列
j = {1, "a", 3}
print(type(j))
s = set()
s = {1, 2, 3, 4, 5, 6,1}
# 追加一个集合
s.update({7,8})
# 删除一个元素
s.remove(2)
# 增加一个元素
s.add(9)
s.add(1)
# 删除一个元素
s.pop()
s1 = {2,4,6,8,10}
# 获取交集
print(s & s1)
# 获取并集
print(s | s1)
# 清空
s.clear()
print(s)
```
## 可变类型与不可变类型
```pycon
# 不可变类型：
    # 1: 数字类型
    # 2：字符串类型
    # 3：元组
    # 4：布尔值
```

```python
# complex 复数
f = 3.14j
print(type(f))
```
# 打印语句
```text
# 创建变量
year = 2024
# 组合打印,默认会使用空格隔开，可以使用sep参数控制
print(year, '年')

# 组合打印 (2024*,年。)
print(year, ',年',sep="*",end="。")

'''
格式化操作符：
    %s: 字符串
    %d: 有符号的十进制整数, %06d 表示输出的整数显示位数是6位，不足的0补齐
    %f: 浮点数, %2f 表示小数位后只显示2位小数
    %%: 输出%
'''
print("现在是%s" % (year))
```
# 输入语句
```text
year = input("请输入年份")
print("你输入的年份是：%s" % (year))
```
# 运算符与表达式
## 算数运算符
```text
+   加    20 + 10 = 30
-   减    20 - 10 = 10
*   乘    20 * 2 = 40
/   除    20 / 2 = 10
//  取整除 9 // 2 = 4
%   取余   9 % 2 = 1
**  幂     2 ** 3 = 8
```
## 赋值运算符
```text
=     直接赋值  a = b
+=    加等      a = a + b
-=    减等      ...
*=    乘等
/=    除等
//=   取整除等
%=    取余等
**=   幂等
```
## 比较运算符
```text
返回值是bool
==   判断等于      a == b
!=   判断不等于    a != b
>    判断大于      a > b
<    判断小于      a < b
>=   判断大于等于   a >= b
<=   判断小于等于   a <= b
```
## 逻辑运算符
```text
and 并且  1<2 and 1>3
or  或  1<2 or 1>3 
not 非  not 1<2
```
## 位运算符
```text
&     按位与运算符     5 & 7  两个数解析成2进制，两个位为1时是1否则是0
|     按位或运算符     5 | 7  两个数解析成2进制，两个位其中一个位是1时是1否则是0
^     按位异或运算符    5 ^ 7 相同位是1不同位是0
~     按位取反运算符    一元运算符位取反
<<    左移运算符       5 << 2 二进制位向左两位
>>    右移运算符       5 >> 2 二进制位向右两位
```
## 成员运算符
```text
in        在指定的序列里查找数据返回bool   3 in (1,2,3,4)
not in    在指定的序列里查找数据返回取反bool   3 in (1,2,3,4)
```
## 身份运算符
```text
is         判断两个标识符是否引用同一个对象返回bool  a,b = 1,1  (a is b)  
is not     is取反
```
# 分支语句
## if分支
```pycon
# if选择语句
weather = "下雨"
if weather == "下雨":
    print("下雨了")
elif weather == "晴天":
    print("天气良好")
else:
    print("未知天气")
```
## match 选择语句
```pycon
x = 10
match x:
    case 1:
        print('x is 1')
    case 2:
        print('x is 2')
    case _:
        print('x is not 1 2')
```
# 循环语句
## for循环
```pycon
for i in range(10):
    print(i)
    if i == 5:
        continue
    if i == 3:
        break
else:
    print("没有执行过break")
```
## while循环
```pycon
a = 10
while a > 0:
    a = a - 1
    if a == 5:
        # 跳过循环
        continue
    print(a)
    if a == 3:
        # 结束循环
        break
else:
    print("没有执行过break")
```
# 异常
```pycon
try:
    a = 2 / 0
    print(a)
except Exception as e:
    print("进入异常")
    print(e)
else:
    print("没有异常执行，可不写")
finally:
    print("有没有异常都执行")
    passwd = input("请输入密码")
    try:
        if len(passwd) < 8:
            raise Exception("密码长度不够")
    except Exception as e:
        print(e)
```
