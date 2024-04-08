# run.py

import sys
sys.path.append('/home/wolfy/Moringa/phase-4/pizza-restaurant-flask-api') 

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

