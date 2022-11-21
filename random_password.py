'''
задание
Створити вью-функцію, яка як параметри отримує імʼя та вік, а повертає фразу: "Привіт, імʼя! Твій пароль: пароль".
Генерувати рандомний пароль, який містить стільки ж знаків, скільки вік користувача.
'''

import random
import string
from flask import Flask, request

app = Flask(__name__)

# url = 'http://127.0.0.1:5000/query?name=Roman&age=10'

@app.route("/query")
def generate_passord():
    passw = ''
    r_age = int(request.args.get('age', default='10'))
    r_name = request.args.get('name', default='Roman')
    for i in range(r_age):
        chr = random.choice(string.ascii_letters)
        passw = passw + chr
    return f'Привет {r_name}, твой пароль: {passw}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)


