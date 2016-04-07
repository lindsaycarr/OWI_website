from owi_website import app
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print ("successfully built static files")
