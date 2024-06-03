# あるURLに対してリクエストがあった際、処理を特定のメソッドに紐付け、処理メソッドを記載
from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# methodsは、このURLに対するHTTPメソッドを制限する、デフォルトは'GET'のみ
@app.route('/', methods=['GET', 'POST'])
def input_salary():
    input_salary = ""
    if request.method == 'POST':
        input_salary = request.form['salary'] # フォームに入力された給与（文字列）

        # 給与チェック！！
        if input_salary == "": # 給与が未入力かどうか
            flash("給与が未入力です。入力してください。")
        elif len(input_salary) > 10: # 入力が10桁までか
            flash("給与には最大9,999,999,999までが入力可能です。")
        elif int(input_salary) < 0: # マイナスの値ではないか
            flash("給与にはマイナスの値は入力できません。")
        else: # 上記じゃなければ、結果のページへGO！
            return redirect(url_for('calc_salary', salary=input_salary))
        
    return render_template('input.html', salary=input_salary)


@app.route('/output', methods=['GET', 'POST'])
def calc_salary():
    # 戻るボタンを押したとき
    if request.method == 'POST':
        return redirect(url_for('input_salary'))
    
    # 給与の計算
    salary = int(request.args.get("salary")) # 給与
    threshold = 1000000
    if salary <= threshold:
        tax_amount = salary * 0.1
    else:
        tax_amount = threshold * 0.1 + (salary - threshold) * 0.2
    pay_amount = salary - tax_amount

    # 表示の変換
    str_salary= "{:,.0f}".format(salary)
    str_pay = "{:,.0f}".format(pay_amount)
    str_tax = "{:,.0f}".format(tax_amount)
    
    return render_template('output.html', salary=str_salary, pay=str_pay, tax=str_tax)