# アプリケーションの環境情報や設定情報を記載

# SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = True

import os
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "mysql"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_DATABASE", "ENSHU")
})
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True # デバックモードをON
# SECRET_KEY = 'secret key' # セッション情報の暗号化
SECRET_KEY = os.urandom(8)
USERNAME = 'john' # ユーザー名
PASSWORD = 'due123' # パスワード