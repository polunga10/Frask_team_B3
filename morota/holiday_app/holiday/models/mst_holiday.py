# データベース定義
from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20))

    def __init__(self, date=None, text=None):
        self.holi_date = date
        self.holi_text = text

    def __repr__(self):
        return '<Entry date:{} text:{}>'.format(self.holi_date, self.holi_text)