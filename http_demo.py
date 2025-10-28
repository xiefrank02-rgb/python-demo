"""
request_examples.py
演示 Python requests 库发送不同类型请求体的方式。
"""

import requests
import json
import msgpack


def send_form_data():
    """
    发送 multipart/form-data 类型数据，通常用于文件上传场景
    此示例中files参数被设置为None，仅作演示
    """
    url = "https://httpbin.org/post"
    files = {'file': open('example.png', 'rb')} if False else None
    data = {'username': 'rank', 'note': 'form-data 示例'}
    response = requests.post(url, files=files, data=data)
    print("=== form-data ===")
    print(response.text, "\n")


def send_x_www_form_urlencoded():
    """
    发送 application/x-www-form-urlencoded 类型数据，
    这是 HTML 表单默认的编码方式，适用于简单的键值对数据
    """
    url = "https://httpbin.org/post"
    data = {'username': 'rank', 'password': '123456'}
    response = requests.post(url, data=data)
    print("=== x-www-form-urlencoded ===")
    print(response.text, "\n")


def send_json():
    """
    发送 application/json 类型数据，
    使用 json 参数自动序列化数据并设置正确的 Content-Type 头部
    """
    url = "https://httpbin.org/post"
    payload = {'username': 'rank', 'password': '123456'}
    response = requests.post(url, json=payload)
    print("=== JSON ===")
    print(response.text, "\n")


def send_xml():
    """
    发送 application/xml 类型数据，
    需要手动设置 Content-Type 头部并提供格式化的 XML 字符串
    """
    url = "https://httpbin.org/post"
    xml_data = """<?xml version="1.0"?>
    <user>
        <username>rank</username>
        <password>123456</password>
    </user>
    """
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=xml_data, headers=headers)
    print("=== XML ===")
    print(response.text, "\n")


def send_binary():
    """
    发送二进制数据，使用 application/octet-stream 类型，
    适用于传输原始字节数据
    """
    url = "https://httpbin.org/post"
    binary_data = b'\x00\x01\x02\x03Hello Binary'
    headers = {'Content-Type': 'application/octet-stream'}
    response = requests.post(url, data=binary_data, headers=headers)
    print("=== Binary ===")
    print(response.text, "\n")


def send_graphql():
    """
    发送 GraphQL 查询，使用 application/graphql 类型，
    适用于与 GraphQL 服务器进行通信
    """
    url = "https://httpbin.org/post"
    query = """
    {
      user(id: 1) {
        username
        email
      }
    }
    """
    headers = {'Content-Type': 'application/graphql'}
    response = requests.post(url, data=query, headers=headers)
    print("=== GraphQL ===")
    print(response.text, "\n")


def send_msgpack():
    """
    发送 MessagePack 格式数据，一种高效的二进制序列化格式，
    类似于 JSON 但更小更快
    """
    url = "https://httpbin.org/post"
    data = {'username': 'rank', 'password': '123456'}
    packed = msgpack.packb(data)
    headers = {'Content-Type': 'application/x-msgpack'}
    response = requests.post(url, data=packed, headers=headers)
    print("=== msgpack ===")
    print(response.text, "\n")


if __name__ == "__main__":
    # 按顺序执行所有示例函数，展示不同类型的 HTTP 请求体发送方式
    send_form_data()
    send_x_www_form_urlencoded()
    send_json()
    send_xml()
    send_binary()
    send_graphql()
    send_msgpack()