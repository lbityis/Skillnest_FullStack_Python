import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask_app import app
from flask_app.controllers import usuarios

if __name__ == "__main__":
    app.run(debug=True)
