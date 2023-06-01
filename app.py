import random
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'unaclavesecretayaleatoria'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice', methods=['POST'])
def practice():
    tables = list(map(int, request.form.getlist('tables')))
    session['selected_tables'] = tables
    return redirect(url_for('next_question'))


@app.route('/check_answer', methods=['POST'])
def check_answer():
    table = int(request.form['table'])
    multiplicando = int(request.form['multiplicando'])
    multiplicador = int(request.form['multiplicador'])
    respuesta = int(request.form['respuesta'])
    tables = list(map(int, request.form.getlist('tables[]')))
    if respuesta == multiplicando * multiplicador:
        return render_template('correct.html', table=table, tables=tables)
    else:
        return render_template('incorrect.html', table=table, multiplicando=multiplicando, multiplicador=multiplicador)


@app.route('/next_question', methods=['GET', 'POST'])
def next_question():
    if request.method == 'POST':
        table = int(request.form['table'])
        multiplicando = int(request.form['multiplicando'])
        multiplicador = int(request.form['multiplicador'])
        respuesta = int(request.form['respuesta'])
        selected_tables = session.get('selected_tables', [])
        if respuesta == multiplicando * multiplicador:
            selected_tables.remove(table)
        if len(selected_tables) == 0:
            return 'Fin de la práctica.'
        else:
            next_table = random.choice(selected_tables)
            next_multiplicando = random.randint(1, 10)
            next_multiplicador = next_table
            session['selected_tables'] = selected_tables
            return render_template('practice.html', tables=selected_tables, table=next_table,
                                   multiplicando=next_multiplicando, multiplicador=next_multiplicador)
    else:
        selected_tables = session.get('selected_tables', [])
        if len(selected_tables) == 0:
            return 'Error: no se han seleccionado tablas.'
        else:
            table = random.choice(selected_tables)
            multiplicando = random.randint(1, 10)
            multiplicador = table
            session['selected_tables'] = selected_tables
            return render_template('practice.html', tables=selected_tables, table=table,
                                   multiplicando=multiplicando, multiplicador=multiplicador)
if __name__ == '__main__':
    app.run()