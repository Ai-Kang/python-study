import json

import requests

if __name__ == '__main__':
    # 指定url
    url = 'https://fanyi.baidu.com/sug'
    # 请求头伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    kw = input("请输入要翻译的内容：")
    data = {
        "kw": kw
    }
    response = requests.post(url=url, data=data, headers=headers)
    response_json = response.json()
    json_file = open('baidu_%s.json' % kw, 'w', encoding='utf-8')
    json.dump(response_json.get("data"), json_file, ensure_ascii=False)
    print(response_json)
    json_file.close()

