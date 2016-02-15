from flask import render_template, request, make_response, redirect, url_for
import yaml
from . import app
from copy import deepcopy

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
    partners_file = open('data/partners.yaml')
    all_partners = yaml.load(partners_file.read())
    return render_template('partners.html', partners=all_partners)


@app.route('/people.html')
@app.route('/people/', endpoint='people-canonical')
def people():
    if request.path == '/people.html':
        return redirect(url_for('people-canonical')), 301
    people_file = open('data/people.yaml')
    all_people = yaml.load(people_file.read())
    people_file.close()
    return render_template('people.html', people = all_people)

@app.route('/people/<person>.html')
@app.route('/people/<person>/', endpoint='person-canonical')
def person(person):
    if request.path == '/people/<person>.html':
        return redirect(url_for('person-canonical', person=person)), 301
    people_file = open('data/people.yaml')
    all_people = yaml.load(people_file.read())
    people_file.close()
    person_record = next((record for record in all_people if record['id'] == person), None)
    if person_record:
        publications = deepcopy(person_record['publications'])
        if publications:
            pubs_list = list(publications.items())
            sorted_pubs = sorted(pubs_list, key=lambda tup: tup[0], reverse=True)
            person_record['publications'] = sorted_pubs
        else:
            person_record['publications'] = None
        presentations = deepcopy(person_record['presentations'])
        if presentations:
            pres_list = list(presentations.items())
            sorted_pres = sorted(pres_list, key=lambda tup: tup[0], reverse=True)
            person_record['presentations'] = sorted_pres
        else:
            person_record['presentations'] = None
        return render_template('person.html', person=person_record)
    else:
        return 404


@app.route('/products.html')
@app.route('/products/', endpoint='products-canonical')
def products():
    if request.path == '/products.html':
        return redirect(url_for('products-canonical')), 301
    products_file = open('data/products.yaml')
    all_products = yaml.load(products_file.read())
    products_file.close()
    return render_template('products.html', products=all_products)

@app.route('/R.html')
@app.route('/R/', endpoint='r-canonical')
def r_home():
    if request.path == '/R.html':
        return redirect(url_for('r-canonical')), 301
    return render_template('R-home.html')


@app.route('/R/about.html')
@app.route('/R/about', endpoint='r-about-canonical')
def r_about():
    if request.path == '/R/about.html':
        return redirect(url_for('r-about-canonical')), 301
    return render_template('R-about.html')



@app.route('/using_owi_tools/')
def examples():
    examples_file = open('data/examples.yaml')
    all_examples = yaml.load(examples_file.read())
    examples_file.close()
    return render_template('examples.html', examples=all_examples)


@app.route('/using_owi_tools/<folder>/')
def example(folder):
    examples_file = open('data/examples.yaml')
    all_examples = yaml.load(examples_file.read())
    examples_file.close()
    example_record = next((record for record in all_examples if record['markdownFolderName'] == folder), None)
    if example_record:
        markdown_file = open('owi_website/static/markdown/'+example_record['markdownFolderName']+'/'+example_record['markdownFileName'])
        markdown_content = markdown_file.read()
        markdown_file.close()
        return render_template('example.html', markdown_content=markdown_content, post_metadata=example_record)
    else:
        return 404

@app.route('/sitemap.xml')
def sitemap_xml():
    sitemap_xml = render_template('sitemap.xml', mimetype='application/xml')
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
