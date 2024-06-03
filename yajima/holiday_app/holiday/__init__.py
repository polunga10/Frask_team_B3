from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemyライブラリのインストール

app = Flask(__name__) # Flaskのアプリケーション本体の作成
# import holiday.views

app.config.from_object("holiday.config") # configファイルの有効化

db = SQLAlchemy(app)

#from holiday.views import views, entries
import holiday.views