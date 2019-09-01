#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app
from flask import Flask
from flask import render_template
from flask import abort
from flask import flash
import os

app = Flask(__name__)  # 创建Flask实例
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/")  # 以装饰器方式定制网址， /为根地址
def index():
    flash("Hello world!")
    flash("Error!", "error")
    return render_template("index.html")  # {{}} 代表静态文件加载和路由生成


# @app.route("/info")  # 会连接到没有找到的页面，所以后面还要加上这个模板页的连接
# def info():
#     return abort(404)
#
#
# @app.errorhandler(404)
# def four_zero_four(err):
#     return render_template("404.html", err=err)


if __name__ == '__main__':
    app.run(debug=True)  # 测试的时候可以写 ，会在页面显示错误
