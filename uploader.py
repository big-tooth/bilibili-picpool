import os, requests
from config import token

# 定义上传函数
def image_upload(file_path):
    # api地址
    api_url = "https://7bu.top/api/upload"

    # 打开图片文件
    with open(file_path, "rb") as f:
        img_file = f.read()

    # 向api发送post请求
    r = requests.post(
        api_url,
        files={"image": (file_path, img_file)},
        params={"token": token},
        timeout=300,
        proxies={"http": "http://127.0.0.1:20172"},
    ).json()

    # 解析返回值，得到图片链接
    if r.get("msg") == "success":
        return r["data"]["url"]


if __name__ == "__main__":
    file_path = os.sys.argv[1]
    print(image_upload(file_path))
