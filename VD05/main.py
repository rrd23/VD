# app.py
from flask import Flask, render_template

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def home():
    # Рендеринг шаблона home.html
    return render_template('home.html')

# Определяем маршрут для страницы "О нас"
@app.route('/about')
def about():
    # Рендеринг шаблона about.html
    return render_template('about.html')

# Запуск приложения
if __name__ == '__main__':
    # Указываем хост и порт для запуска приложения
    app.run(debug=True)

