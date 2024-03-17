# Задание
# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    name = request.cookies.get('name')
    if name:
        return redirect('/welcome')
    return render_template('hw_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    resp = make_response(redirect('/welcome'))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)
    return resp

@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if not name:
        return redirect('/')
    return render_template('hw_welcome.html', name=name)

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp

if __name__ == '__main__':
    app.run(debug=True)

