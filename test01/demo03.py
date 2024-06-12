for i in range(10):
    print(i)
    if i == 5:
        continue
    if i == 3:
        break
else:
    print("没有执行过break")
