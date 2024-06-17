class Animal(object):
    # 构造函数
    def __init__(self, name):
        print("__init__被调用")
        self.name = name

    # toStr方法
    def __str__(self):
        return self.name

    # 调用+号时的重写
    def __add__(self, other):
       return self.name + other.name

    # 比较函数
    def __eq__(self, other):
        return self.name == other.name
animal = Animal("JOJO")
