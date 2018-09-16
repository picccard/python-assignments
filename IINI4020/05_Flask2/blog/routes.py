from flask import render_template, url_for, flash, redirect
from blog import app, db
from blog.forms import ArticleForm
from blog.models import Article


'''
Grabs all the articles in the DB, turns the list around and renders
'''
@app.route('/')
@app.route('/home')
@app.route('/news')
def display_news():
    articles = Article.query.all()
    # Turns the list around so the newest entries comes on top
    articles = reversed(articles)
    return render_template('news.html', title='News', articles=articles)

'''
Creates an ArticleForm, if the form is submitted then the data is saved to the DB
and we returns to the news-page with a successfull notification.
If the form is not submitted, it just gets presented.
'''
@app.route('/news/add', methods=['GET', 'POST'])
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        # Creates the article and saves it to the DB
        article = Article(title=form.title.data, content=form.content.data, author=form.author.data)
        db.session.add(article)
        db.session.commit()
        # Feedback and redirect to all news
        flash('Your article has been created!', 'success')
        return redirect(url_for('display_news'))
    # Regular GET-requests just gets the empty form
    return render_template('create-article.html', title='Add News Article', legend='New Article', form=form)
