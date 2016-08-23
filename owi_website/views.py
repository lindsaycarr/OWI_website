from flask import render_template
import yaml
from . import app
from copy import deepcopy
from pprint import pprint



@app.route('/', endpoint='home-canonical')
def home():
    return render_template('index.html')


@app.route('/careers/', endpoint='careers-canonical')
def careers():
    return render_template('careers.html')

@app.route('/partners/', endpoint='partners-canonical')
def partners():
    partners_file = open('data/partners.yaml')
    all_partners = yaml.safe_load(partners_file.read())
    partners_file.close()
    return render_template('partners.html', partners=all_partners)


@app.route('/people/', endpoint='people-canonical')
def people():
    people_file = open('data/people.yaml')
    all_people = yaml.safe_load(people_file.read())
    people_file.close()
    just_people = []
    for person in all_people:
        if 'Office' not in person['id']:
            just_people.append(person)
    return render_template('people.html', people=just_people)


@app.route('/people/<person>/', endpoint='person-canonical')
def person(person):
    people_file = open('data/people.yaml')
    all_people = yaml.safe_load(people_file.read())
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


@app.route('/products/', endpoint='products-canonical')
def products():
    products_file = open('data/products.yaml')
    all_products = yaml.safe_load(products_file.read())
    products_file.close()
    return render_template('products.html', products=all_products)

