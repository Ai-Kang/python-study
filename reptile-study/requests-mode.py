# request模块学习
"""
urllib: 比较古老
request:
    环境安装：pip install requests
    1: 指定url
    2： 发起请求
    3: 获取响应数据
    4: 解析数据
"""
import  requests
if __name__ == '__main__':
    # 指定url
    url  = 'https://www.sogou.com'
    # 发起请求
    r = requests.get(url=url)
    # 获取响应数据
    context = r.text
    # 存储到本地文件
    with open('sogou.html', 'w', encoding='utf-8') as f:
        f.write(context)
    print("爬取成功")


