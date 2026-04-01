from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
# Use the final public URL path for GitHub Pages deployment.
app.config['FREEZER_BASE_URL'] = 'https://victor-villacis.github.io/matrixPokedex/'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()