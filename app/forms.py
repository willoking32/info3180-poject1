from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms import SelectMultipleField, FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired

class create_prop(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    bedrooms = IntegerField('number of Bedrooms',validators=[InputRequired()])
    bathrooms = IntegerField('number of Bathrooms',validators=[InputRequired()])
    location = StringField('Title',validators=[InputRequired()])
    price = IntegerField('Price',validators=[InputRequired()])
    disc = TextAreaField('Discription')
    ptype = SelectMultipleField('Type of sale',choices=['Apartment','House'],
                                    validators=[DataRequired()])
    photo = FileField('Image Upload', 
                    validators=[FileRequired(), 
                                FileAllowed(['jpeg','jpg','png'], 'Images Only!')])
