# あるURLに対してリクエストがあった際、処理を特定のメソッドに紐付け、処理メソッドを記載
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

# デコレータ: あるメソッドを実行する前に特定の処理を実行させる
# ログインしているかしていないかの判定
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'): # ログインしていないとき
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# methodsは、このURLに対するHTTPメソッドを制限する、デフォルトは'GET'のみ
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST': # POST（送信）のとき
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else: # ログインが成功したら
            session['logged_in'] = True
            flash('ログインしました')
            return redirect('/')
    return render_template('login.html') # GET（URLにアクセス）のとき？


@app.route('/logout')
def logout():
    session.pop('logged_in', None) # セッション情報を削除
    flash('ログアウトしました')
    return redirect('/') # ホーム画面に戻る