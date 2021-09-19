from flask import render_template
from app import app
from flask import app


@app.errorhandler(404)
def four_0_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('four0four.html'), 404
