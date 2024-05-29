from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":
        input_salary = request.form["salary"]
        # if input_salary is None:
        #     flash("給与が未入力です。入力してください。")
        # elif input_salary > 9999999999:
        #     flash("給与には最大9,999,999,999まで入力可能です。")
        # elif input_salary < 0:
        #     flash("給与にはマイナスの値は入力できません。")
        # else:
        #     return redirect('output.html', salary=calcsalary(input_salary))  
        return redirect(url_for('output', salary=input_salary))
    return render_template('input.html')

@app.route('/output', methods=["GET", "POST"])
def output():
    salary = int(request.args.get('salary'))
    if salary <= 1000000:
        tax = salary * 0.1
    else:
        tax = (salary - 1000000) * 0.2
        tax += 1000000 * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
    allowance = salary - tax

    a_salary = "{:,}".format(salary)
    a_allowance = "{:,}".format(allowance)
    a_tax = "{:,}".format(tax)

    if request.method == "POST":
        return redirect('input.html')
    return render_template("output.html", salary=a_salary, allowance=a_allowance, tax=a_tax)

# def calcsalary (salary):
#     #税金の計算
#     if salary <= 1000000:
#         tax = salary * 0.1
#     else:
#         tax = (salary - 1000000) * 0.2
#         tax += 1000000 * 0.1

#     #税金の四捨五入の計算
#     tax = Decimal(str(tax)).quantize(Decimal("0"),
#         rounding = ROUND_HALF_UP)

#     #支給額の計算
#     allowance = salary - tax

#     #戻り値
#     return salary, allowance, tax
