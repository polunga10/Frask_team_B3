# あるURLに対してリクエストがあった際、処理を特定のメソッドに紐付け、処理メソッドを記載
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required


# 現在存在する全てのブログ記事をデータベースから取得し、返す
@app.route('/')
@login_required
def show_entries():
    # データベースからすべての記事を取得し、新しく記事が作られた順に並べる
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)


# 投稿内容を受信してデータベースに保存
@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    # モデルインスタンスの作成
    entry = Entry(
        title=request.form['title'],
        text = request.form['text']
    )
    # モデルインスタンスをデータベースに保存
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))


# 新規投稿のリンク/new_entryにアクセスしたとき
# ブログ投稿フォームを返す
@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')

@app.route('/entries/<int:id>', methods=['GET'])
@login_required
def show_entry(id):
    entry = Entry.query.get(id) # idの記事をデータベースから取得
    return render_template('entries/show.html', entry=entry)

# 編集ボタンが押されたら編集画面を返す
@app.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

# 編集内容を受け取り、データベースを更新する
@app.route('/entries/<int:id>/update', methods=['POST'])
@login_required
def update_entry(id):
    entry = Entry.query.get(id) # idで記事を取得
    entry.title = request.form['title'] # タイトルの更新
    entry.text = request.form['text'] # 本文の更新
    db.session.merge(entry) # 更新のときはmerge
    db.session.commit() # データベースの更新
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

# 削除ボタンが押されたとき、削除する
@app.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry) # データベースの内容を削除
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))