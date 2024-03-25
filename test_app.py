import unittest
from app import app, db, User, WheelCommand  # Import additional models as needed
from flask_testing import TestCase

class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""
    
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class UserTestCase(BaseTestCase):

    def test_create_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/users',
                json={
                    'username': 'testuser',
                    'password_hash': 'testpassword',
                    'role': 'testrole'
                }
            )
            self.assertEqual(response.status_code, 201)
            self.assertIn('New user created', response.json['message'])

    def test_get_users(self):
        """Ensure get all users behaves correctly."""
        with self.client:
            self.client.post(
                '/users',
                json={
                    'username': 'testuser',
                    'password_hash': 'testpassword',
                    'role': 'testrole'
                }
            )
            response = self.client.get('/users')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json['users']), 1)
            user = response.json['users'][0]
            self.assertEqual(user['username'], 'testuser')

# Add more test cases for WheelCommand
class WheelCommandTestCase(BaseTestCase):

    def test_add_wheel_command(self):
        """Ensure a new wheel command can be added."""
        with self.client:
            response = self.client.post(
                '/wheelCommands',
                json={
                    'speed': 100,
                    'direction': 'forward',
                    'duration': 10
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_wheel_commands(self):
        """Ensure get all wheel commands behaves correctly."""
        with self.client:
            self.client.post(
                '/wheelCommands',
                json={
                    'speed': 100,
                    'direction': 'forward',
                    'duration': 10
                }
            )
            response = self.client.get('/wheelCommands')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            command = response.json[0]
            self.assertEqual(command['speed'], 100)
            self.assertEqual(command['direction'], 'forward')
            self.assertEqual(command['duration'], 10)

# Add more test cases for LiDARScan
class LiDARScanTestCase(BaseTestCase):

    def test_add_lidar_scan(self):
        """Ensure a new LiDAR scan can be added."""
        with self.client:
            response = self.client.post(
                '/lidarScans',
                json={
                    'distance_readings': '15,30,45'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_lidar_scans(self):
        """Ensure get all LiDAR scans behaves correctly."""
        with self.client:
            self.client.post(
                '/lidarScans',
                json={
                    'distance_readings': '15,30,45'
                }
            )
            response = self.client.get('/lidarScans')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            scan = response.json[0]
            self.assertEqual(scan['distance_readings'], '15,30,45')

# Test cases for CameraFeed
class CameraFeedTestCase(BaseTestCase):

    def test_add_camera_feed(self):
        """Ensure a new camera feed can be added."""
        with self.client:
            response = self.client.post(
                '/cameraFeeds',
                json={
                    'image': 'image_data_base64',
                    'description': 'Test camera feed'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_camera_feeds(self):
        """Ensure all camera feeds can be retrieved."""
        with self.client:
            self.client.post(
                '/cameraFeeds',
                json={
                    'image': 'image_data_base64',
                    'description': 'Test camera feed'
                }
            )
            response = self.client.get('/cameraFeeds')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)

# Test cases for DetectedObject
class DetectedObjectTestCase(BaseTestCase):

    def test_add_detected_object(self):
        """Ensure a new detected object can be added."""
        with self.client:
            response = self.client.post(
                '/detectedObjects',
                json={
                    'camera_feed_id': 1,
                    'object_type': 'Vehicle',
                    'confidence': 0.9,
                    'position': 'x1,y1,x2,y2'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_detected_objects(self):
        """Ensure all detected objects can be retrieved."""
        with self.client:
            self.client.post(
                '/detectedObjects',
                json={
                    'camera_feed_id': 1,
                    'object_type': 'Vehicle',
                    'confidence': 0.9,
                    'position': 'x1,y1,x2,y2'
                }
            )
            response = self.client.get('/detectedObjects')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            detected_object = response.json[0]
            self.assertEqual(detected_object['object_type'], 'Vehicle')
            self.assertEqual(detected_object['confidence'], 0.9)
            self.assertEqual(detected_object['position'], 'x1,y1,x2,y2')

# Test cases for NavigationRoute
class NavigationRouteTestCase(BaseTestCase):

    def test_add_navigation_route(self):
        """Ensure a new navigation route can be added."""
        with self.client:
            response = self.client.post(
                '/navigationRoutes',
                json={
                    'start_point': 'Start',
                    'end_point': 'End'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_navigation_routes(self):
        """Ensure all navigation routes can be retrieved."""
        with self.client:
            self.client.post(
                '/navigationRoutes',
                json={
                    'start_point': 'Start',
                    'end_point': 'End'
                }
            )
            response = self.client.get('/navigationRoutes')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            navigation_route = response.json[0]
            self.assertEqual(navigation_route['start_point'], 'Start')
            self.assertEqual(navigation_route['end_point'], 'End')

# Test cases for CollisionEvent
class CollisionEventTestCase(BaseTestCase):

    def test_add_collision_event(self):
        """Ensure a new collision event can be added."""
        with self.client:
            response = self.client.post(
                '/collisionEvents',
                json={
                    'severity': 4,
                    'description': 'Minor scrape'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_collision_events(self):
        """Ensure all collision events can be retrieved."""
        with self.client:
            self.client.post(
                '/collisionEvents',
                json={
                    'severity': 4,
                    'description': 'Minor scrape'
                }
            )
            response = self.client.get('/collisionEvents')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            collision_event = response.json[0]
            self.assertEqual(collision_event['severity'], 4)
            self.assertEqual(collision_event['description'], 'Minor scrape')

# Test cases for SystemHealth
class SystemHealthTestCase(BaseTestCase):

    def test_add_system_health(self):
        """Ensure a new system health record can be added."""
        with self.client:
            response = self.client.post(
                '/systemHealth',
                json={
                    'component': 'Sensor',
                    'status': 'Operational',
                    'notes': 'Fully functional'
                }
            )
            self.assertEqual(response.status_code, 201)

    def test_get_system_healths(self):
        """Ensure all system health records can be retrieved."""
        with self.client:
            self.client.post(
                '/systemHealth',
                json={
                    'component': 'Sensor',
                    'status': 'Operational',
                    'notes': 'Fully functional'
                }
            )
            response = self.client.get('/systemHealth')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            system_health = response.json[0]
            self.assertEqual(system_health['component'], 'Sensor')
            self.assertEqual(system_health['status'], 'Operational')
            self.assertEqual(system_health['notes'], 'Fully functional')

if __name__ == '__main__':
    unittest.main()
