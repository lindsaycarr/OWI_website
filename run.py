import argparse
from owi_website import app
from flask_frozen import Freezer
from flaskext.markdown import Markdown


freezer = Freezer(app)

if __name__ == '__main__':


    Markdown(app,
              extensions=['fenced_code', 'tables', 'codehilite'],
              extension_configs={},
              output_format='html5',)
    if app.config['FREEZE']:
        freezer.freeze()
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', '-ht', type=str)
    args = parser.parse_args()
    host_val = args.host
    if host_val is not None:
        host = host_val
    else:
        host = '127.0.0.1'
    app.run(host=host, port=5050, threaded=True)
    # run from the command line as follows
    # python runserver.py -ht <ip address of your choice>