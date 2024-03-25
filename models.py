# models.py
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(80), nullable=False)

class WheelCommand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    speed = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class LiDARScan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    distance_readings = db.Column(db.Text, nullable=False)

class CameraFeed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.LargeBinary, nullable=True)
    description = db.Column(db.String(255), nullable=True)

class DetectedObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_feed_id = db.Column(db.Integer, db.ForeignKey('camera_feed.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    object_type = db.Column(db.String(80), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    position = db.Column(db.String(100), nullable=False)

class NavigationRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_point = db.Column(db.String(100), nullable=False)
    end_point = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CollisionEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    severity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)

class SystemHealth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    component = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    notes = db.Column(db.String(255), nullable=True)