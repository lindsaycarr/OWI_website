import argparse
from owi_website import app as application
from flask_frozen import Freezer
from flaskext.markdown import Markdown



freezer = Freezer(application)



if __name__ == '__main__':

    #freezer.freeze()
    Markdown(application,
              extensions=['fenced_code', 'tables', 'codehilite'],
              extension_configs={},
              safe_mode=True,
              output_format='html',)
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', '-ht', type=str)
    args = parser.parse_args()
    host_val = args.host
    if host_val is not None:
        host = host_val
    else:
        host = '127.0.0.1'
    application.run(host=host, port=5050)
    # run from the command line as follows
    # python runserver.py -ht <ip address of your choice>