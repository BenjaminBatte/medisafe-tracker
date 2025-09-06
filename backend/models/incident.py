import enum
from extensions import db

class SeverityEnum(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Incident(db.Model):
    __tablename__ = "incidents"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  

    user = db.relationship("User", backref=db.backref("incidents", lazy=True))