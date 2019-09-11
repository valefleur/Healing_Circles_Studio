from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init and define schema for db
db = SQLAlchemy(app)


class poses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # image = db.Column(db.Blob) # TODO how to store an image
    # TODO how expensive are images in Heroku?  Cheaper alternatives?
    # Expecting ~25 images in db
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    stretched = db.Column(db.String(500))
    worked = db.Column(db.String(500))

    def __repr__(self):
        return '<Task %r>; % self.id'


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/learn', methods=['GET'])
def learn_more():
    return 'This is the Learn More page! It is still TBD.'


@app.route('/book', methods=['GET'])
def book_a_class():
    return 'This is the Book a Class page! It is still TBD.'


@app.route('/pics', methods=['GET'])
def pictures():
    return render_template('Pics.html')


if __name__ == '__main__':
    app.run(debug=True)
