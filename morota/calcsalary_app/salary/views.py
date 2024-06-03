from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":
        if request.form["salary"] == "":
            flash("給与が未入力です。入力してください。")
        elif int(request.form["salary"]) > 9999999999:
            flash("給与には最大9,999,999,999まで入力可能です。")
        elif int(request.form["salary"]) < 0:
            flash("給与にはマイナスの値は入力できません。")
        else:
            input_salary = request.form["salary"]
            return redirect(url_for('output', salary=input_salary))
    return render_template('input.html')

@app.route('/output', methods=["GET", "POST"])
def output():
    salary = int(request.args.get('salary'))
    if salary <= 1000000:   #税金の計算
        tax = salary * 0.1
    else:
        tax = (salary - 1000000) * 0.2
        tax += 1000000 * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP) #税金の四捨五入の計算
    allowance = salary - tax    #支給額の計算

    a_salary = "{:,}".format(salary)
    a_allowance = "{:,}".format(allowance)
    a_tax = "{:,}".format(tax)
        
    return render_template("output.html", salary=a_salary, allowance=a_allowance, tax=a_tax)

