from datetime import datetime
from apps.app import db

class Text(db.Model):
    __tablename__ = "texts"

    id = db.Column(db.Integer, primary_key=True)
    textword = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
