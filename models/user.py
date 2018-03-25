from models import db

class User(db.Model):
    uuid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(255))
    facebook_id = db.Column(db.BigInteger)

    def __init__(self, uuid, name, email, facebook_id):
        self.uuid = uuid
        self.name = name
        self.email = email
        self.facebook_id = facebook_id
