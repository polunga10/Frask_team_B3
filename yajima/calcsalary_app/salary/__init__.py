from flask import Flask
app = Flask(__name__) # Flaskのアプリケーション本体の作成
import salary.views

app.config.from_object("salary.config") # configファイルの有効化