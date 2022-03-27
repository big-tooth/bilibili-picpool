# bilibili-picpool

## 简介: 

- 使用7bu作为后端的图床
- Demo: ~~https://pic.aya1.top~~ （可以作为网页打开，也可作为api）（服务器到期，已经无了）

## 注意事项:

- 合理使用, 请勿滥用, 如有后果概不负责

#### 环境需求:

python >= 3.6

#### 第三方库:

flask, requests, werkzeug

#### 使用方法:

根据文档获取token
https://7bu.top/index/api.html

**使用例:**

1. 在当前文件夹执行`python uploader.py <图片路径>`

```bash
❯ python uploader.py test.png
https://bu.dusays.com/2022/03/27/4ded92e8bc041.png
```


2. 在当前文件夹执行`python app.py`运行flask接口，然后使用post上传图片，获得图片地址

```bash
# shell命令
# 可以在 ~/.zshrc 里自定义函数实现快捷上传 bpic(){curl -F "file=@$1" https://pic.aya1.top/short}

❯ curl http://127.0.0.1:2000 -F "file=@test.png" 
https://bu.dusays.com/2022/03/27/86d37347fc80e.png
```

```python
# python脚本

import requests

response = requests.post(
    "http://127.0.0.1:2000", files={"file": open("test.png", "rb")}
)

print(response.text)

# 运行结果
https://bu.dusays.com/2022/03/27/86d37347fc80e.png

```

```bash
# 或浏览器直接打开http://127.0.0.1:2000，根据提示操作
```
