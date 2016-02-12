from flask import render_template, request, make_response, redirect, url_for

from . import app


@app.route('/index.html')
@app.route('/', endpoint='home-canonical')
def home():
    if request.path == '/index.html':
        return redirect(url_for('home-canonical')), 301
    return render_template('index.html')


@app.route('/careers.html')
@app.route('/careers/', endpoint='careers-canonical')
def careers():
    if request.path == '/careers.html':
        return redirect(url_for('careers-canonical')), 301
    return render_template('careers.html')

@app.route('/datascience.html')
@app.route('/datascience/', endpoint='datascience-canonical')
def datascience():
    if request.path == '/datascience.html':
        return redirect(url_for('datascience-canonical')), 301
    return render_template('datascience.html')

@app.route('/partners.html')
@app.route('/partners/', endpoint='partners-canonical')
def partners():
    if request.path == '/partners.html':
        return redirect(url_for('partners-canonical')), 301
    return render_template('partners.html')


@app.route('/people.html')
@app.route('/people/', endpoint='people-canonical')
def people():
    if request.path == '/people.html':
        return redirect(url_for('people-canonical')), 301
    return render_template('people.html')


@app.route('/products.html')
@app.route('/products/', endpoint='products-canonical')
def products():
    if request.path == '/products.html':
        return redirect(url_for('products-canonical')), 301
    return render_template('products.html')

@app.route('/sitemap.xml')
def sitemap_xml():
    return render_template('sitemap.xml')
