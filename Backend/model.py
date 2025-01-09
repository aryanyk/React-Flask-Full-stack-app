from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

    def to_json(self):
        return {
            'id': self.id,
            'firstNname': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }