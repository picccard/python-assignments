from flask import Flask, render_template, url_for
app = Flask(__name__)

news = [
    {
        'author': 'eskil',
        'title': 'First news article',
        'date_posted': 'September 15, 2018',
        'content': 'This is the first news article'
    },
    {
        'author': 'not eskil',
        'title': 'Second news article',
        'date_posted': 'September 16, 2018',
        'content': 'This is the second news article'
    }
]

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/')
@app.route('/add-news')
def add_news():
    return render_template('add-news.html', title='Add News Article')

@app.route('/news')
def display_news():
    return render_template('news.html', title='News', news=news)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
