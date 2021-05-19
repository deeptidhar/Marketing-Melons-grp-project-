"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def marketplace_landing():
    """Get marketplace landing page."""

    return render_template("marketplace.html")


# @app.route('/melons')
# def all_melons():
#     """View all melons."""

#     melons = crud.get_melons()

    # return render_template('all_melons.html', melons=melons)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)