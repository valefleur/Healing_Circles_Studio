from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/learn')
def learn_more():
    return 'This is the Learn More page! It is still TBD.'


@app.route('/book')
def book_a_class():
    return 'This is the Book a Class page! It is still TBD.'


if __name__ == '__main__':
    app.run(debug=True)
