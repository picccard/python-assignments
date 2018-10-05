import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import ArticleForm, RegistrationForm, LoginForm, UpdateAccountForm
from blog.models import Article, User
from flask_login import login_user, current_user, logout_user, login_required


'''
Grabs all the articles in the DB, turns the list around and renders
'''
@app.route('/')
@app.route('/home')
@app.route('/news')
@login_required
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
        article = Article(title=form.title.data, content=form.content.data, user_id=1) #author=form.author.data
        db.session.add(article)
        db.session.commit()
        # Feedback and redirect to all news
        flash('Your article has been created!', 'success')
        return redirect(url_for('display_news'))
    # Regular GET-requests just gets the empty form
    return render_template('create-article.html', title='Add News Article', legend='New Article', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('display_news'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account for {form.username.data} created!', category='success')
        redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('display_news'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('display_news'))
        else:
            flash('Login Unsuccessful. Check email and password.', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('display_news'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                                image_file=image_file, form=form)
