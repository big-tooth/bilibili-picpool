#!/usr/bin/env python3
# Auther: Ayatale

import os
from config import host, port
from datetime import timedelta
from uploader import image_upload
from werkzeug.utils import secure_filename
from flask import Flask, url_for, request, redirect, render_template

# 启动flask
app = Flask(__name__)

# 定义图片的保存路径
base_path = os.path.join(os.path.dirname(__file__), "static", "img")

# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)

# 设置允许的文件格式
ALLOWED = set(["jpg", "png", "jpeg", "gif", "JPG", "PNG", "JPEG", "GIF"])
ERROR = "请检查上传的图片类型，仅限于jpg、png、gif"


# 判断文件是否为图片
def check_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED


# 图片保存函数
def save_img():
    img = request.files["file"]
    # 检查图片格式
    if not (img and check_file(img.filename)):
        return
    # 保存图片
    img_name = secure_filename(img.filename)
    save_path = os.path.join(base_path, img_name)
    img.save(save_path)
    return save_path


# 设置网页后端
@app.route("/upload", methods=["POST", "GET"])
def upload_web():
    if request.method == "POST":
        save_path = save_img()
        if not save_path:
            return render_template("index.html")
        # 上传到B站
        result_url = image_upload(save_path)
        # 显示结果
        return {"code": "success", "data": {"url": result_url}}
    return render_template("index.html")


# 设置api接口
@app.route("/", methods=["POST", "GET"])
def upload_full():
    # 如果是浏览器访问则跳转至路由/upload
    if request.method == "GET":
        return redirect(url_for("upload_web"))
    # 保存图片
    save_path = save_img()
    if not save_path:
        return ERROR
    # 调用上传函数，返回图片链接
    return image_upload(save_path)


@app.route("/favicon<ico>")
def return_logo():
    return "Null"


if __name__ == "__main__":
    app.run(host=host, port=port, debug=1, threaded=1)
