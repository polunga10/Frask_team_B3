from flask import request, redirect, url_for, render_template, flash, session
from decimal import Decimal, ROUND_HALF_UP
from salary import app

@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        salary = request.form['salary']

        if not salary :
            flash("給与が未入力です.")
            return render_template('input.html')
        
##        if not salary.isdigit():
  ##          flash("数字を入力してください")
    ##        return render_template('input.html')    
        
        for_judge = int(salary)

        if for_judge >= 9999999999:
            flash("給与には最大9,999,999,999,999まで入力可能です")
            return render_template('input.html')
        
        if for_judge < 0 :
            flash("給与にはマイナスの値は入力できません。")
            return render_template('input.html')       
            
        return redirect(url_for('output_salary', salary=salary))        
    return render_template('input.html')

@app.route('/output',methods=['GET', 'POST'])
def output_salary():
    salary = request.args.get('salary', None)
    TrueSalary = int(salary)
    TrueSalary = "{:,}".format(TrueSalary)
    if salary is not None:
        salary = int(salary)
        if salary > 1000000:  # 給料が100万円を超える場合
            over_million = salary - 1000000  # 100万を超える部分を計算
            over_tax = over_million * 0.2 + 100000
            over_tax = Decimal(str(over_tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
            salary = salary - over_tax
            tax = int(over_tax)
            formatted_tax = "{:,}".format(tax)
        else:  # 給料が100万円以下の場合
            tax = salary * 0.1
            tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
            salary = salary - tax
            tax = int(tax)
            formatted_tax = "{:,}".format(tax)
        formatted_salary = "{:,}".format(salary)
    else:
        salary = tax = None

    if request.method == 'POST':
        return redirect("/")    
    return render_template('output.html', get = TrueSalary,salary=formatted_salary, tax=formatted_tax)
