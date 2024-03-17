from pathlib import PurePath, Path

from flask import Flask, request, render_template, abort, redirect, flash, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename

MIN_AGE = 18

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/next')
def next_page():
    context = {
        'task': 'Задание №1',
        'description': 'Создать страницу, на которой будет кнопка "Нажми меня", '
                       'при нажатии на которую будет переход на другую страницу '
                       'с приветствием пользователя по имени.'
    }
    return render_template('page_1.html', **context)


@app.route('/upload_image/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    context = {
        'task': 'Задание 2',
        'description': 'Создать страницу, на которой будет изображение и ссылка на другую страницу, '
                       'на которой будет отображаться форма для загрузки изображений.'
    }
    return render_template('upload.html', **context)


@app.route('/login_password/', methods=['GET', 'POST'])
def login_password():
    context = {
        'task': 'Задание 3',
        'description': 'Создать страницу, на которой будет форма для ввода логина и пароля '
                       'При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и '
                       'пароля и переход на страницу приветствия пользователя или страницу с ошибкой.'
    }
    login_dict = {
        'login': '1@1.ru',
        'password': '123'
    }
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == login_dict['login'] and password == login_dict['password']:
            return f"Login success - {escape(login)}"
        else:
            return 'Error'
    return render_template('login.html', **context)


@app.route('/text_count/', methods=['GET', 'POST'])
def text_count():
    context = {
        'task': 'Задание №4',
        'description': 'Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"'
                       'При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.'
    }
    if request.method == 'POST':
        text = request.form.get('text').split()
        return f'Words: {len(text)}'
    return render_template('text_count.html', **context)


@app.route('/math_simple/', methods=['GET', 'POST'])
def math_simple():
    context = {
        'task': 'Задание №5',
        'description': 'Создать страницу, на которой будет форма для ввода двух чисел и выбор операции '
                       '(сложение, вычитание, умножение или деление) и кнопка "Вычислить" '
                       'При нажатии на кнопку будет произведено вычисление'
                       'результата выбранной операции и переход на страницу с результатом.'
    }
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')
        if operation == 'plus':
            return f'Result: {int(num1) + int(num2)}'
        if operation == 'minus':
            return f'Result: {int(num1) - int(num2)}'
        if operation == 'mult':
            return f'Result: {int(num1) * int(num2)}'
        if operation == 'div':
            try:
                return f'Result: {int(num1) / int(num2)}'
            except:
                return "Can't divide by 0"

    return render_template('math_simple.html', **context)


@app.route('/verify_age/', methods=['GET', 'POST'])
def verify_age():
    context = {
        'task': 'Задание №6',
        'description': 'Создать страницу, на которой будет форма для ввода имени '
                       'и возраста пользователя и кнопка "Отправить"'
                       'При нажатии на кнопку будет произведена проверка'
                       'возраста и переход на страницу с результатом или на'
                       'страницу с ошибкой в случае некорректного возраста.'
    }
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if MIN_AGE < age:
            return f'{name}, добро пожаловать!'
        else:
            abort(403)
    return render_template('verify_age.html', **context)


@app.route('/redirect/', methods=['GET', 'POST'])
def redirect():
    context = {
        'task': 'Задание №7',
        'description': 'Создать страницу, на которой будет форма для ввода числа'
                       'и кнопка "Отправить"'
                       'При нажатии на кнопку будет произведено'
                       'перенаправление на страницу с результатом, где будет'
                       'выведено введенное число и его квадрат.'
    }
    if request.method == 'POST':
        if not request.form['number']:
            flash('Enter number!', 'danger')
            return redirect(url_for('quadro'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('qaudro'))
    return render_template('form.html', **context)

@app.route('/form/', methods=['GET', 'POST'])
def form():
    return render_template('quadro.html')

@app.errorhandler(403)
def page_not_found(e):
    context = {
        'title': 'Access Denied due to age',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403


if __name__ == '__main__':
    app.run(debug=True)
