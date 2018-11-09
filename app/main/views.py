from flask import render_template,request,redirect,url_for
from app import *
# from ..request import get_news
from ..request import get_news,get_articles
from ..models import Review
from .forms import ReviewForm
# Review = reviews.Review
from . import main
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #getting news
    news = get_news()
    print(news)
    title = 'FRANCO NEWS'
    return render_template('index.html', title = title, news = news)


@main.route('/news/<id>')
def news(id):

    final_articles = get_articles(id)
    return render_template('news.html',final_articles = final_articles )  