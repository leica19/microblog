
from flask import render_template
from app import app, db
import random

@app.errorhandler(404)
def not_found_error(error):
    pattern = random.randint(1, 2)
    return render_template('404.html', pattern=pattern), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
