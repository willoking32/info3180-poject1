from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms import SelectField, FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired

class create_prop(FlaskForm):
    title = StringField('Property Title',validators=[InputRequired()])
    bedrooms = IntegerField('No. of Bedrooms',validators=[InputRequired()])
    bathrooms = IntegerField('No. of Bathrooms',validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    price = IntegerField('Price',validators=[InputRequired()])
    disc = TextAreaField('Discription')
    ptype = SelectField('Type of sale',choices=['House', 'Apartment'],
                                    validators=[DataRequired()])
    photo = FileField('Image Upload', 
                    validators=[FileRequired(), 
                                FileAllowed(['jpeg','jpg','png'], 'Images Only!')])
