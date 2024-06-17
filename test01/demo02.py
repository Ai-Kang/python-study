# 读取csv
import csv

with open("data.csv",mode="r",encoding="gbk") as f:
    csv_reader = csv.reader(f)
    for e in csv_reader:
        print(e)
