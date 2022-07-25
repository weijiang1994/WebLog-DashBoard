"""
coding:utf-8
file: extensions.py
@time: 2022/7/25 22:41
@desc:
"""
from flask_celery import Celery
from flask_sqlalchemy import SQLAlchemy

task = Celery()
db = SQLAlchemy()
