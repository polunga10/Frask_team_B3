from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablenme__ = 'entries' # テーブルの名前
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()
    
    # 参照されたときのコンソールでの出力形式
    def __repr__(self):
        return f'<Entry id:{self.id} title:{self.title} text:{self.text}'
