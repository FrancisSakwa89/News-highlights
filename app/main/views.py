from flask import render_template
from . import main

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)der_template('index.html')

@app.route('/news/<news_id>')
def movie(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)    

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('movie.html',id = new_id)
    