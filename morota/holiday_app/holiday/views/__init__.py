from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from functools import wraps
from holiday import db
from holiday.models.mst_holiday import Holiday

# 入力画面の呼び出し
@app.route("/", methods=["GET", "POST"])
def show_entries():
    if request.method=="POST":
        h_date = request.form['holiday']
        h_text = request.form['holiday_text']
        button = request.form["button"]
        return redirect(url_for("show_result", holiday_date=h_date, holiday_text=h_text, button=button))
    return render_template("input.html")



# 登録、更新、削除のデータベース処理、その後の結果画面の呼び出し
@app.route("/maintenance_data", methods=["GET", "POST"])
def show_result():
    date=request.args.get('holiday_date')
    text=request.args.get('holiday_text')
    button=request.args.get('button')

    if button == "insert_update":
        if db.session.query(Holiday).filter_by(holi_date=date).first() == None:
            # データの保存
            holiday = Holiday(
                date=date,
                text=text
            )
            db.session.add(holiday)
            db.session.commit()
        else:
            # データの更新
            holiday = db.session.query(Holiday).filter_by(holi_date=date).first()
            holiday.holi_text = text
            db.session.add(holiday)
            db.session.commit()

    elif button == "delete":
        #データの削除
        db.session.query(Holiday).filter_by(holi_date=date).delete()
        db.session.commit()

    if request.method=="POST":
        return redirect(url_for("show_entries"))
    
    #次回は表示メッセージを作って送れるように変更する↓
    return render_template("result.html", holiday=holiday)





# 一覧画面の呼び出し
@app.route("/list", methods=["GET", "POST"])
def show_list():
    return render_template("list.html")





