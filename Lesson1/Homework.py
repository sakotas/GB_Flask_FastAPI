# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hw_base.html')


@app.route('/clothes/')
def clothes():
    context = [{'title': 'Футболка',
                'comment': 'Удобная футболка',
                'price': 12.99,
                },
               {'title': 'Штаны',
                'comment': 'Неудобные штаны',
                'price': 15.98,
                },
               {'title': 'Трусы',
                'comment': 'Шелковые трусики танго',
                'price': 3.00,
                }, ]
    return render_template('hw_clothes.html', context=context)


@app.route('/boots/')
def boots():
    context = [{'title': 'Кроссовки',
                'comment': 'Красивые',
                'price': 1.99,
                },
               {'title': 'Кеды',
                'comment': 'Удобные',
                'price': 115.98,
                },
               {'title': 'Тапочки',
                'comment': 'Вьетнамки',
                'price': 3.90,
                }, ]
    return render_template('hw_boots.html', context=context)


@app.route('/coats/')
def coats():
    context = [{'title': 'Пальто',
                'comment': 'Из шерсти чубаки',
                'price': 1112.99,
                },
               {'title': 'Бомбер',
                'comment': 'Бомбит',
                'price': 154.98,
                },
               {'title': 'Кожанка',
                'comment': 'Хтыщ Хтыщ',
                'price': 333.33,
                }, ]
    return render_template('hw_coats.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
