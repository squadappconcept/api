from models import db

class Session(db.Model):
    uuid = db.Column(db.String(36), primary_key=True)
    user_uuid = db.Column(db.String(36))

    def __init__(self, uuid, user_uuid=None):
        self.uuid = uuid
        self.user_uuid = user_uuid
