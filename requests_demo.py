import requests

def check(resp,word):
    result = word.lower() in resp.lower()
    print(word,result)

if __name__ == "__main__":
    url = 'http://fat-irs.juanhandapi.com/api/getDefinedVars'
    response = requests.get(url)
    resp_text = response.text
    print(response.status_code)
    # print(response.text)
    with open("check_words.txt", 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符
    for word in words:
        check(resp_text,word)
