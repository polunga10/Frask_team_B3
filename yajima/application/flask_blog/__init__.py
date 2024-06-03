from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemyライブラリのインストール

app = Flask(__name__) # Flaskのアプリケーション本体の作成
import flask_blog.views.views

app.config.from_object("flask_blog.config") # configファイルの有効化

db = SQLAlchemy(app)

from flask_blog.views import views, entries