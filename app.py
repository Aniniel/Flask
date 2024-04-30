from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Función para cargar datos desde el archivo JSON
def load_data():
    with open('data.json', 'r', encoding='utf-8') as file:  # Asegúrate de usar la codificación utf-8
        return json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/xxxs', methods=['GET', 'POST'])
def xxxs():
    data = load_data()
    search_query = request.form.get('search', '').lower() if request.method == 'POST' else ''
    filtered_data = [anime for anime in data if search_query in anime['title']['text'].lower()]
    return render_template('xxxs.html', xxxs=filtered_data, search_query=search_query)

@app.route('/xxx/<int:id>')
def xxx_detail(id):
    data = load_data()
    anime = next((item for item in data if item['id'] == id), None)
    if anime:
        return render_template('xxx_detail.html', anime=anime)
    else:
        return "404 Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)