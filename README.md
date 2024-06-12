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

```python
# complex 复数
f = 3.14j
print(type(f))
```
```python
# list 列表
g = [1, 2, "a", "b"]
print(type(g))
```
```python
# tuple 元组
h = (1, "2", "a")
print(type(h))
```
```python
# set 集合,不重复序列
j = {1, "a", 3}
print(type(j))
```
```python
# dict 字典
l = {"name": "aikang", "age": 23}
print(type(l))
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
