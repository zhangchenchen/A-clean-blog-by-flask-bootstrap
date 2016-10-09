# clean blog

## what's this

a small blog coding by flask &amp; bootstrap, keep simple and clean  

## tech stack
 - backend: flask
 - frontend: bootstrap
 - database: mysql + SQLAlchemy
 - server: Nignx + WSGI 

## quick guide

- git clone this project
- edit config.py #set up module db mysql connection info
- setup virtual python environment(2.7) with virtualenv and activate
- pip install -r requirements
- rm -rf migrations
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade
- python manage.py runserver

## development log

- 2016.10.7-8 :



## deploy



# 简易博客

## 简介

这是一个由flask 与 bootstrap开发的非常轻量的博客。

## 技术栈

- 后端：flask
- 前端：bootstrap
- 数据库：mysql + SQLAlchemy
- 服务器：Nignx + WSGI 


## 快速使用

- 使用git clone下整个项目 
- 编辑 config.py #配置MySQL数据库连接信息
- 使用virtualenv 设置Python2.7的虚拟环境并激活
- pip install -r requirements 
- rm -rf migrations
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade
- python manage.py runserver

##开发日志


