from flask import render_template, request, make_response, redirect, url_for
import yaml
from . import app
from copy import deepcopy
from utils import pull_full_feed, pull_youtube_info



@app.route('/', endpoint='home-canonical')
def home():
    return render_template('index.html')


@app.route('/careers/', endpoint='careers-canonical')
def careers():
    return render_template('careers.html')


@app.route('/datascience/', endpoint='datascience-canonical')
def datascience():
    return render_template('datascience.html')


@app.route('/partners/', endpoint='partners-canonical')
def partners():
    partners_file = open('data/partners.yaml')
    all_partners = yaml.load(partners_file.read())
    return render_template('partners.html', partners=all_partners)


@app.route('/people/', endpoint='people-canonical')
def people():
    people_file = open('data/people.yaml')
    all_people = yaml.load(people_file.read())
    people_file.close()
    del all_people[0]
    return render_template('people.html', people=all_people)


@app.route('/people/<person>/', endpoint='person-canonical')
def person(person):
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


@app.route('/products/', endpoint='products-canonical')
def products():
    products_file = open('data/products.yaml')
    all_products = yaml.load(products_file.read())
    products_file.close()
    return render_template('products.html', products=all_products)


@app.route('/R/', endpoint='r-canonical')
def r_home():
    return render_template('R-home.html')


@app.route('/R/about', endpoint='r-about-canonical')
def r_about():
    return render_template('R-about.html')


@app.route('/training/')
def examples():
    examples_file = open('data/examples.yaml')
    all_examples = yaml.load(examples_file.read())
    examples_file.close()
    return render_template('examples.html', examples=all_examples)


@app.route('/training/<folder>/')
def example(folder):
    examples_file = open('data/examples.yaml')
    all_examples = yaml.load(examples_file.read())
    examples_file.close()
    example_record = next((record for record in all_examples if record['markdownFolderName'] == folder), None)
    if example_record:
        markdown_file = open('owi_website/static/markdown/'+example_record['markdownFolderName']+'/'
                             +example_record['markdownFileName'])
        markdown_content = markdown_file.read()
        markdown_file.close()
        return render_template('example.html', markdown_content=markdown_content, post_metadata=example_record)
    else:
        return 404


@app.route('/blog/')
def blog():
    feed_url = 'https://internal.cida.usgs.gov/wiki/createrssfeed.action?types=blogpost&spaces=PUBSWI&title=USGS+-+CIDA+RSS+Feed&labelString=owi_news&excludedSpaceKeys%3D&sort=modified&maxResults=10&timeSpan=300&showContent=true&confirm=Create+RSS+Feed'
    posts = pull_full_feed(feed_url)
    return render_template('blog.html', posts=posts)


@app.route('/videos/')
def videos():
    videos_file = open('data/videos.yaml')
    videos = yaml.load(videos_file.read())
    videos_file.close()
    video_metadata= []
    for video_url in videos['youtube']:
        video_metadata.append(pull_youtube_info(video_url))
    return render_template('videos.html', video_metadata=video_metadata)


@app.route('/sitemap.xml')
def sitemap_xml():
    sitemap_xml_content = render_template('sitemap.xml', mimetype='application/xml')
    response = make_response(sitemap_xml_content)
    response.headers["Content-Type"] = "application/xml"
    return response
