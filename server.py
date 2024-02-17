
# Файл server.py

from flask import Flask, jsonify, render_template
app = Flask(__name__)

# Пример данных о хоккейных матчах
hockey_matches = [
    {
        'homeTeam': 'Красная Машина',
        'awayTeam': 'Ледяные акулы',
        'date': '2022-10-15'
    },
    {
        'homeTeam': 'Летающие клюшки',
        'awayTeam': 'Разбитые шлемы',
        'date': '2022-11-02'
    }
]

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint для получения данных о матчах
@app.route('/api/hockey/matches', methods=['GET'])
def get_hockey_matches():
    return jsonify(hockey_matches)

if __name__ == '__main__':
    app.run()