import httpx

url = 'https://httpbin.org/post'
data = {'key': 'value'}

# 发起 POST 请求，使用 stream=True 以便于流式处理
with httpx.Client() as client:
    response = client.post(url, data=data, stream=True)

    # 调用 .read() 来读取流式内容
    content = response.read()
    print(content)  # 或者进一步处理
