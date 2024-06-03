from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Entry


@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST': 
        if request.form["button"] == "insert_update":
            entry = Entry(
                holi_date = request.form['date'],
                holi_text = request.form['text']
            )        
            db.session.add(entry)
            db.session.commit()   
            return redirect(url_for('result',entry = entry)) 
        if request.form["button"] == "delete":
            entry = Entry.query.filter_by(
            holi_date=request.form['date'],
            holi_text=request.form['text']
            ).first()
            if entry is not None:
                db.session.delete(entry)
                db.session.commit()
                return redirect(url_for('delete'))
        if request.form["button"] == "list":
            return redirect(url_for('list'))    
    return render_template('input.html')


@app.route('/result', methods=['GET'])
def result():
    if request.method == 'GET':
        return redirect(url_for('input'))
    return render_template('result.html')


@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'GET':
        return redirect(url_for('input'))
    return render_template('list.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        return redirect(url_for('input'))
    return render_template('delete.html')
