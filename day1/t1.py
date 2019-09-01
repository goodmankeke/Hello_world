#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app

from flask import Flask
from flask import render_template

app = Flask(__name__)  # 创建Flask实例


@app.route("/")  # 以装饰器方式定制网址， /为根地址
def index():
    return render_template("index.html") # 要放在根目录的APP下


if __name__ == '__main__':
    app.run(debug=True)  # 测试的时候可以写 ，会在页面显示错误
