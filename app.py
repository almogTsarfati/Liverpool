from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), unique=True, nullable=False)
    rank = db.Column(db.String(2), unique=True, nullable=False)

    def __repr__(self):
        return f"Player('{self.fullname}, '{self.rank}, {self.id})"


posts = [
    {
        'name': 'Stevie G',
        'id': 1,
        'rank': 10
    },
    {
        'name': 'sir Kenny Dalglish',
        'id': 2,
        'rank': 10
    }
]


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
    # new_player = {"name": request.form['name'], 'rank': request.form['rank'], 'id': request.form['id']}
    print(Player.query.all())
    # posts.append(new_player)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
