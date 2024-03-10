# Задание №1.
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Привет, Мир!'


# Задание №2.
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".
@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def contact():
    return 'Contact'


# Задание №3.
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.
@app.route('/sum_num/<int:num_1>/<int:num_2>/')
def sum_num(num_1, num_2):
    return f'Sum: {num_1 + num_2}'


# Задание №4.
# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
@app.route('/count/<string:input_string>/')
def count_str(input_string):
    return f'Length: {len(input_string)}'


# Задание №5.
# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!
# @app.route('/index/')
# def html_index():
#     return render_template('index.html')


# Задание №6.
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.
@app.route('/students/')
def students():
    _students = [{'name': 'Никанор',
                  'surname': 'Иванов',
                  'age': 17,
                  'rating': '4',
                  },
                 {'name': 'Иван',
                  'surname': 'Сидоров',
                  'age': 23,
                  'rating': '5',
                  },
                 {'name': 'Урюк',
                  'surname': 'Хай',
                  'age': 83,
                  'rating': '2',
                  }, ]
    context = {'users': _students}
    return render_template('students.html', **context)


# Задание №7.
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.
@app.route('/news/')
def news():
    context = [{'title': 'Новость 1',
                'content': 'Кошка родила котят',
                'release_date': '10-02-2024',
                },
               {'title': 'Новость 2',
                'content': 'Собака родила щенят',
                'release_date': '10-03-2024',
                },
               {'title': 'Новость 3',
                'content': 'Лягушка родила лягушат',
                'release_date': '11-01-2023',
                }, ]
    return render_template('news.html', context=context)


# Задание №8.
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.
# @app.route('/task8/')
# def task8():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
