# 定义函数
def test01():
    print("test01")


# 定义带参函数
def sum(number1, number2):
    return number1 + number2


# 定义默认值函数
def sum1(number1, number2=2, number3=3):
    return number1 + number2 + number3


# 可变参数
def sum2(*args):
    count = 0;
    for num in args:
        count += num
    return count

# 可接受字典的可变参数
def sum3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# 调用函数，调用必须在定义之后
test01()
print(sum2(1, 2, 3))

# 定义全局变量
num1 = 10
def sum4():
    global num1
    num1 = 20
    print(num1)
sum4()
print(num1)

# 匿名函数
fun = lambda x,y: x+y
print(fun(1,2))
