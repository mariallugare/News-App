from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_all_news
from ..models import Article


@main.route('/')
@main.route('/home')
def home():
    name ='Marial'
    news = get_all_news()
    return render_template('index.html', news=news,name=name)