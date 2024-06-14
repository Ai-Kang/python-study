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
