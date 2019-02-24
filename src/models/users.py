class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    userType = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.userType}')"
