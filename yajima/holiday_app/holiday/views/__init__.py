# あるURLに対してリクエストがあった際、処理を特定のメソッドに紐付け、処理メソッドを記載
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models import Holiday
from functools import wraps


@app.route('/', methods=['GET', 'POST'])
def input_entry():
    if request.method == 'POST':
        button = request.form["button"]
        if button == "check_date":
            # 日付検索
            date = request.form['holiday']
            return redirect(url_for("show_result", date=date, button=button))
        elif button == "check_text":
            # テキスト検索
            text = request.form['holiday_text']
            return redirect(url_for("show_list", text=text, button=button))
        elif button == "insert_update":
            # 新規登録・更新時の処理
            date = request.form['holiday']
            text = request.form['holiday_text']
            return redirect(url_for("show_result", date=date,text=text, button=button))
        elif button == "delete":
            # 削除の処理
            date = request.form['holiday']
            return redirect(url_for("show_result", date=date, button=button))
        elif button == "show_list":
            # 一覧出力
            return redirect(url_for("show_list", button=button))
    return render_template('input.html')

@app.route('/maintenance_date', methods=['GET', 'POST'])
def show_result():
    if request.method == 'POST':
        return redirect(url_for("input_entry"))
    if request.args.get("button") == "check_date":
        # 日付検索
        # データが存在するかどうかを確認
        holiday = Holiday.query.filter_by(holi_date=request.args.get("date")).first()
        if holiday is not None:
            flash(f"{holiday.holi_date}は「{holiday.holi_text}」です")
            return redirect(url_for("input_entry"))
        else:
            flash(f"{request.args.get('date')}は、祝日マスタに登録されてません")
            return redirect(url_for("input_entry"))

    # 新規登録・更新
    if request.args.get("button")=="insert_update":
        holiday = Holiday.query.filter_by(holi_date=request.args.get("date")).first()
        if holiday is not None:
            # データが存在する→更新
            holiday.holi_text = request.args.get("text")
        else:
            # データが存在しない→新規登録
            holiday = Holiday(
                holi_date = request.args.get("date"),
                holi_text = request.args.get("text")
            )
        db.session.add(holiday)
        db.session.commit()
        message = f"{holiday.holi_date}は「{holiday.holi_text}」に更新されました"

    elif request.args.get("button") == "delete":
        # holiday = Holiday.query.get(request.args.get('date'))
        holiday = Holiday.query.filter_by(holi_date=request.args.get("date")).first()
        if holiday is not None:
            db.session.delete(holiday) # データベースの内容を削除
            db.session.commit()
            message = f"{holiday.holi_date}（{holiday.holi_text}）は、削除されました"
        else:
            # 登録されていない場合
            flash(f"{request.args.get('date')}は、祝日マスタに登録されてません")
            return redirect(url_for("input_entry"))
    return render_template('result.html', message = message)

# 一覧表示
@app.route('/list', methods=['GET', 'POST'])
def show_list():
    if request.method == 'POST':
        return redirect(url_for("input_entry"))
    if request.args.get("button") == "check_text":
        # テキスト検索
        holidays = Holiday.query.filter(Holiday.holi_text.ilike(f'%{request.args.get("text")}%')).all()
    else:
        # 一覧表示
        holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)