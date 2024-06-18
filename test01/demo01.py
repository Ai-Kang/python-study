import json

# 构建一个大的 JSON 数据结构
data = {
    "metadata": {
        "description": "Large JSON data example for demonstration.",
        "size": "Approximately 5M"
    },
    "data": []
}

# 为了使 JSON 大小接近5M，重复添加数据直到达到预期大小
while len(json.dumps(data)) < 2 * 1024 * 1024:
    # 添加一些简单的键值对来增加 JSON 的大小
    for i in range(1000):
        data["data"].append({
            "id": i,
            "name": f"Student_{i}",
            "age": 20 + i % 5,
            "major": "Computer Science" if i % 3 == 0 else "Engineering"
        })

# 转换为 JSON 字符串
json_str = json.dumps(data)

# 输出生成的 JSON 字符串大小
print(f"Generated JSON string size: {len(json_str)} bytes")
f = open("jsonTest.json",mode="w",encoding="utf-8")
f.write(json_str)
f.close()
# 可选：输出部分 JSON 字符串内容
# print(json_str)  # 输出前500个字符示例
