from flask import Flask, render_template
import utile.data as data

app = Flask(__name__)

@app.route('/')
def home():
    animes = data.fetch_animes_from_db()
    return render_template('index.html', animes=animes)

if __name__ == '__main__':
    app.run(debug=True)