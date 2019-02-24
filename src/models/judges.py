class Judges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judgeName = db.Column(db.String(80), unique=True, nullable=False)
    totalMoney = db.Column(db.Integer)

    def __repr__(self):
        return f"Judge('{self.judgeName}', '{self.totalMoney}')"
