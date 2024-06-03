# あるURLに対してリクエストがあった際、処理を特定のメソッドに紐付け、処理メソッドを記載
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models import Holiday
from functools import wraps


@app.route('/', methods=['GET', 'POST'])
def input_entry():
    if request.method == 'POST':
        date = request.form['holiday']
        text = request.form['holiday_text']
        button = request.form["button"]
        return redirect(url_for("show_result", date=date,text=text, button=button))
    return render_template('input.html')

@app.route('/maintenance_date', methods=['GET', 'POST'])
def show_result():
    if request.method == 'POST':
        return redirect(url_for("input_entry"))
    
    # 新規登録
    # if文が反応していない？？？？<----------------やる！！
    if request.args.get("button")=="insert_update":
        holiday = Holiday(
            holi_date = request.args.get("date"),
            holi_text = request.args.get("text")
            )
        db.session.add(holiday)
        db.session.commit()
        message = f"{holiday.holi_date}は「{holiday.holi_text}」に更新されました"
    return render_template('result.html', message = message)

@app.route('/list', methods=['GET', 'POST'])
def show_list():
    if request.method == 'POST':
        return redirect(url_for("input_entry"))
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)


# # デコレータ: あるメソッドを実行する前に特定の処理を実行させる
# # ログインしているかしていないかの判定
# def login_required(view):
#     @wraps(view)
#     def inner(*args, **kwargs):
#         if not session.get('logged_in'): # ログインしていないとき
#             return redirect(url_for('login'))
#         return view(*args, **kwargs)
#     return inner

# # methodsは、このURLに対するHTTPメソッドを制限する、デフォルトは'GET'のみ
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST': # POST（送信）のとき
#         if request.form['username'] != app.config['USERNAME']:
#             flash('ユーザ名が異なります')
#         elif request.form['password'] != app.config['PASSWORD']:
#             flash('パスワードが異なります')
#         else: # ログインが成功したら
#             session['logged_in'] = True
#             flash('ログインしました')
#             return redirect('/')
#     return render_template('login.html') # GET（URLにアクセス）のとき？


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None) # セッション情報を削除
#     flash('ログアウトしました')
#     return redirect('/') # ホーム画面に戻る