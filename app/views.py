"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import create_prop
from app.models import sales
from sqlalchemy import func


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


#created
#error 405 method not allowed if 'POST' only
@app.route('/properties/create', methods=['POST', 'GET'])
def propc():
    cprop = create_prop()
    if cprop.validate_on_submit():
        title =cprop.title.data
        bedrooms = cprop.bedrooms.data
        bathrooms = cprop.bathrooms.data
        location = cprop.location.data
        ptype = cprop.ptype.data
        price = cprop.price.data
        disc = cprop.disc.data
        photo = cprop.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        id = id_get()
        if id:
            id= id + 1
        else:
            id = 1

        prop = sales(id,title,bedrooms,bathrooms,location,price,ptype,filename,disc)

        db.session.add(prop)
        db.session.commit()

        flash('Property Added', 'success')
        return redirect(url_for('plist'))

    return render_template('add_property.html',form = cprop)


def id_get():
    return db.session.query(func.max(sales.propertyid)).scalar()


#created
@app.route('/properties', methods = ['GET', 'POST'])
def plist():
    i = 1
    o = id_get()
    total_props =db.session.execute(db.select(sales.propertyid,sales.title,
                                            sales.bedrooms,sales.bathrooms,
                                            sales.location,sales.ptype,sales.price,
                                            sales.disc,sales.photo).order_by(sales.propertyid)).fetchall()
        
    #if total_props:
    #flash(total_props)
    return render_template('propertylist.html',props = total_props)

    #return render_template('propertylist.html')


#helps plist() to retrieve images
@app.route('/getpic/<filename>')
def get_pic(filename):
    return send_from_directory(os.path.join(os.getcwd(),
                                            app.config['UPLOAD_FOLDER']), filename)



#created
@app.route('/properties/<propertyid>', methods = ['GET'])
def propview(propertyid):
    a_prop =  db.session.execute(db.select(sales.propertyid,sales.title,
                                            sales.bedrooms,sales.bathrooms,
                                            sales.location,sales.ptype,sales.price,
                                            sales.disc,sales.photo).filter_by(propertyid = propertyid)).fetchall()
    flash(a_prop)

    return render_template('property.html', shown = a_prop)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
