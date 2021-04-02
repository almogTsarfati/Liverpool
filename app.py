from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #'mysql://root:Aa@127.0.0.1:3306/db' test 5
db = SQLAlchemy(app)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), unique=True, nullable=False)
    rank = db.Column(db.String(2), unique=True, nullable=False)

    def __repr__(self):
        return f"Player('{self.fullname}, '{self.rank}, {self.id})"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/players')
def players():
    # db.session.remove(Player.query.all())
    players = Player.query.all()
    return render_template('players.html', posts=players)


@app.route('/add', methods=['POST'])
def add():
    new_player = Player(fullname=request.form['name'], rank=request.form['rank'])
    db.session.add(new_player)
    db.session.commit()
    print(Player.query.all())
    return redirect(url_for('home'))


@app.route('/health')
def health_check():
    return "true"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
