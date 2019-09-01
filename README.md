# Hello_world
just a flask study Thanks

github的第一次使用搭建，和Flask框架的一些小学习。

## jiaja2模板的使用
1. 继承：{% extends “父模板路径” %}
2. 数据块：{% block 块名 %} 。。。{% endblock %}
3. 路由生成：{{ url_for(“模块名.视图名”) }}
4. 静态文件加载 {{ url_for(‘static’, filename=”静态文件路径”) }}
5. 条件语句：{% if 条件 %}。。。{% endif %}
