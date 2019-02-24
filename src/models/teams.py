class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(80), unique=True, nullable=False)
    teamDescription = db.Column(db.String(500), nullable=False)
    teamPhoto = db.Column(db.String(20), nullable=False, default='team_photo.jpg')
    totalPoints = db.Column(db.Integer)

    def __repr__(self):
        return f"Team('{self.teamName}', '{self.totalPoints}')" 
