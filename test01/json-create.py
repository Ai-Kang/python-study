import json

# 构建一个大的 JSON 数据结构
data = {
    "metadata": {
        "description": "Large JSON data for testing purposes.",
        "size": "5M or more"
    },
    "data": []
}

# 生成大量数据直到 JSON 字符串超过5M字节
while len(json.dumps(data)) < 5 * 1024 * 1024:
    data["data"].append({
        "key": "value"
    })

# 转换为 JSON 字符串
json_str = json.dumps(data)

# 输出生成的 JSON 字符串大小
print(f"Generated JSON string size: {len(json_str)} bytes")

# 可选：输出部分 JSON 字符串内容
print(json_str[:500])  # 输出前500个字符示例
