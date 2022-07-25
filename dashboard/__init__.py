"""
coding:utf-8
file: __init__.py
@time: 2022/7/25 22:41
@desc:
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Weblog DashBoard's System Design By Flask!"

    return app
