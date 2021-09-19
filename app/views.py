from flask import render_template
from flask import app
from .request import get_article, get_sources
from app import app

# Views
@app.route('/')
def index():

    generalNews_source = get_sources('general')
    businessNews_source = get_sources('business')
    techNews_source = get_sources('technology')
    entertainmentNews_source = get_sources('entertainment')
    healthNews_source = get_sources('health')
    sportsNews_source = get_sources('sports')
    title = 'Welcome'
    return render_template('index.html', title=title, general=generalNews_source, business=businessNews_source, technology=techNews_source, entertainment=entertainmentNews_source, sports=sportsNews_source, health=healthNews_source)


@app.route('/source/<source_id>')
def article(source_id):

    return render_template('index.html', id=source_id)


@app.route('/source/<int:id>')
def source(id):

    source = get_sources(id)
    title = f'{source.title}'

    return render_template('news.html', title=title, source=source)


@app.route('/articles/<id>')
def article(id):

    article = get_article(id)
    title = f'{id}'

    return render_template('news.html', title=title, article=article)
