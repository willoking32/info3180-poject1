from . import db

from werkzeug.security import generate_password_hash

#heavily influenced by lab 4
class sales(db.Model):

    __tablename__ = "property_list"

    propertyid = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    ptype = db.Column(db.String(10))
    price = db.Column(db.Integer)
    disc = db.Column(db.String(255))
    photo = db.Column(db.String(80))
    

    def __init__(self,propertyid, title, bedrooms, bathrooms, location, price, ptype, photo, disc ):
        self.propertyid = propertyid
        self.title = title
        self.bedrooms = bedrooms 
        self.bathrooms = bathrooms
        self.location = location
        self.ptype = ptype
        self.price = price
        self.photo = photo
        self.discription = disc
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.propertyid)  # python 2 support
        except NameError:
            return str(self.propertyid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.title)