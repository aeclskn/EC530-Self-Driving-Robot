from flask import Blueprint, request, jsonify
from .models import db, User, WheelCommand, LiDARScan, CameraFeed, DetectedObject, NavigationRoute, CollisionEvent, SystemHealth

crud = Blueprint('crud', __name__)
# CRUD operations
# Users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], password_hash=data['password_hash'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'New user created'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'role': user.role} for user in users]), 200

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.password_hash = data.get('password_hash', user.password_hash)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'User updated'}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'}), 200

# WheelCommands
@app.route('/wheelCommands', methods=['POST'])
def create_wheel_command():
    data = request.get_json()
    command = WheelCommand(speed=data['speed'], direction=data['direction'], duration=data['duration'])
    db.session.add(command)
    db.session.commit()
    return jsonify({'message': 'WheelCommand created'}), 201

@app.route('/wheelCommands', methods=['GET'])
def get_wheel_commands():
    commands = WheelCommand.query.all()
    return jsonify([{'id': cmd.id, 'speed': cmd.speed, 'direction': cmd.direction, 'duration': cmd.duration} for cmd in commands]), 200

@app.route('/wheelCommands/<int:id>', methods=['PUT'])
def update_wheel_command(id):
    command = WheelCommand.query.get_or_404(id)
    data = request.get_json()
    command.speed = data.get('speed', command.speed)
    command.direction = data.get('direction', command.direction)
    command.duration = data.get('duration', command.duration)
    db.session.commit()
    return jsonify({'message': 'WheelCommand updated'}), 200

@app.route('/wheelCommands/int:id', methods=['DELETE'])
def delete_wheel_command(id):
    command = WheelCommand.query.get_or_404(id)
    db.session.delete(command)
    db.session.commit()
    return jsonify({'message': 'WheelCommand deleted'}), 200

@app.route('/lidarScans', methods=['POST'])
def create_lidar_scan():
    data = request.get_json()
    scan = LiDARScan(distance_readings=data['distance_readings'])
    db.session.add(scan)
    db.session.commit()
    return jsonify({'message': 'LiDARScan created'}), 201

@app.route('/lidarScans', methods=['GET'])
def get_lidar_scans():
    scans = LiDARScan.query.all()
    return jsonify([{'id': scan.id, 'distance_readings': scan.distance_readings} for scan in scans]), 200

@app.route('/lidarScans/<int:id>', methods=['PUT'])
def update_lidar_scan(id):
    scan = LiDARScan.query.get_or_404(id)
    data = request.get_json()
    scan.distance_readings = data.get('distance_readings', scan.distance_readings)
    db.session.commit()
    return jsonify({'message': 'LiDARScan updated'}), 200

@app.route('/lidarScans/<int:id>', methods=['DELETE'])
def delete_lidar_scan(id):
    scan = LiDARScan.query.get_or_404(id)
    db.session.delete(scan)
    db.session.commit()
    return jsonify({'message': 'LiDARScan deleted'}), 200

# CRUD operations for CameraFeed
@app.route('/cameraFeeds', methods=['POST'])
def create_camera_feed():
    data = request.get_json()
    feed = CameraFeed(timestamp=datetime.utcnow(), image=data['image'], description=data['description'])
    db.session.add(feed)
    db.session.commit()
    return jsonify({'message': 'CameraFeed created'}), 201

@app.route('/cameraFeeds', methods=['GET'])
def get_camera_feeds():
    feeds = CameraFeed.query.all()
    return jsonify([{'id': feed.id, 'timestamp': feed.timestamp, 'description': feed.description} for feed in feeds]), 200

@app.route('/cameraFeeds/<int:id>', methods=['PUT'])
def update_camera_feed(id):
    feed = CameraFeed.query.get_or_404(id)
    data = request.get_json()
    feed.image = data.get('image', feed.image)
    feed.description = data.get('description', feed.description)
    db.session.commit()
    return jsonify({'message': 'CameraFeed updated'}), 200

@app.route('/cameraFeeds/<int:id>', methods=['DELETE'])
def delete_camera_feed(id):
    feed = CameraFeed.query.get_or_404(id)
    db.session.delete(feed)
    db.session.commit()
    return jsonify({'message': 'CameraFeed deleted'}), 200

# CRUD operations for DetectedObject
@app.route('/detectedObjects', methods=['POST'])
def create_detected_object():
    data = request.get_json()
    detected_object = DetectedObject(camera_feed_id=data['camera_feed_id'], timestamp=datetime.utcnow(), object_type=data['object_type'], confidence=data['confidence'], position=data['position'])
    db.session.add(detected_object)
    db.session.commit()
    return jsonify({'message': 'DetectedObject created'}), 201

@app.route('/detectedObjects', methods=['GET'])
def get_detected_objects():
    objects = DetectedObject.query.all()
    return jsonify([{'id': obj.id, 'camera_feed_id': obj.camera_feed_id, 'object_type': obj.object_type, 'confidence': obj.confidence, 'position': obj.position} for obj in objects]), 200

@app.route('/detectedObjects/<int:id>', methods=['PUT'])
def update_detected_object(id):
    obj = DetectedObject.query.get_or_404(id)
    data = request.get_json()
    obj.object_type = data.get('object_type', obj.object_type)
    obj.confidence = data.get('confidence', obj.confidence)
    obj.position = data.get('position', obj.position)
    db.session.commit()
    return jsonify({'message': 'DetectedObject updated'}), 200

@app.route('/detectedObjects/<int:id>', methods=['DELETE'])
def delete_detected_object(id):
    obj = DetectedObject.query.get_or_404(id)
    db.session.delete(obj)
    db.session.commit()
    return jsonify({'message': 'DetectedObject deleted'}), 200

# CRUD operations for NavigationRoute
@app.route('/navigationRoutes', methods=['POST'])
def create_navigation_route():
    data = request.get_json()
    navigation_route = NavigationRoute(start_point=data['start_point'], end_point=data['end_point'], created_at=datetime.utcnow())
    db.session.add(navigation_route)
    db.session.commit()
    return jsonify({'message': 'NavigationRoute created'}), 201

@app.route('/navigationRoutes', methods=['GET'])
def get_navigation_routes():
    routes = NavigationRoute.query.all()
    return jsonify([{'id': route.id, 'start_point': route.start_point, 'end_point': route.end_point} for route in routes]), 200

@app.route('/navigationRoutes/<int:id>', methods=['PUT'])
def update_navigation_route(id):
    route = NavigationRoute.query.get_or_404(id)
    data = request.get_json()
    route.start_point = data.get('start_point', route.start_point)
    route.end_point = data.get('end_point', route.end_point)
    db.session.commit()
    return jsonify({'message': 'NavigationRoute updated'}), 200

@app.route('/navigationRoutes/<int:id>', methods=['DELETE'])
def delete_navigation_route(id):
    route = NavigationRoute.query.get_or_404(id)
    db.session.delete(route)
    db.session.commit()
    return jsonify({'message': 'NavigationRoute deleted'}), 200

# CRUD operations for CollisionEvent
@app.route('/collisionEvents', methods=['POST'])
def create_collision_event():
    data = request.get_json()
    collision_event = CollisionEvent(timestamp=datetime.utcnow(), severity=data['severity'], description=data['description'])
    db.session.add(collision_event)
    db.session.commit()
    return jsonify({'message': 'CollisionEvent created'}), 201

@app.route('/collisionEvents', methods=['GET'])
def get_collision_events():
    events = CollisionEvent.query.all()
    return jsonify([{'id': event.id, 'timestamp': event.timestamp, 'severity': event.severity, 'description': event.description} for event in events]), 200

@app.route('/collisionEvents/<int:id>', methods=['PUT'])
def update_collision_event(id):
    event = CollisionEvent.query.get_or_404(id)
    data = request.get_json()
    event.severity = data.get('severity', event.severity)
    event.description = data.get('description', event.description)
    db.session.commit()
    return jsonify({'message': 'CollisionEvent updated'}), 200

@app.route('/collisionEvents/<int:id>', methods=['DELETE'])
def delete_collision_event(id):
    event = CollisionEvent.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'CollisionEvent deleted'}), 200

# CRUD operations for SystemHealth
@app.route('/systemHealth', methods=['POST'])
def create_system_health():
    data = request.get_json()
    system_health = SystemHealth(timestamp=datetime.utcnow(), component=data['component'], status=data['status'], notes=data['notes'])
    db.session.add(system_health)
    db.session.commit()
    return jsonify({'message': 'SystemHealth record created'}), 201

@app.route('/systemHealth', methods=['GET'])
def get_system_health_records():
    records = SystemHealth.query.all()
    return jsonify([{'id': record.id, 'timestamp': record.timestamp, 'component': record.component, 'status': record.status, 'notes': record.notes} for record in records]), 200

@app.route('/systemHealth/<int:id>', methods=['PUT'])
def update_system_health(id):
    record = SystemHealth.query.get_or_404(id)
    data = request.get_json()
    record.component = data.get('component', record.component)
    record.status = data.get('status', record.status)
    record.notes = data.get('notes', record.notes)
    db.session.commit()
    return jsonify({'message': 'SystemHealth record updated'}), 200

@app.route('/systemHealth/<int:id>', methods=['DELETE'])
def delete_system_health(id):
    record = SystemHealth.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'SystemHealth record deleted'}), 200