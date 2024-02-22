
-- Authentication and Authorization Module
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE AccessLogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    action TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users(id)
);

-- Wheel Module
CREATE TABLE WheelCommands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    speed INTEGER,
    direction TEXT,
    duration INTEGER
);

-- LiDAR Module
CREATE TABLE LiDARScans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    distance_readings TEXT  
);

-- Camera Module
CREATE TABLE CameraFeeds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    image BLOB,
    description TEXT
);

-- Visual Object Detection Module
CREATE TABLE DetectedObjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    camera_feed_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    object_type TEXT,
    confidence REAL,
    position TEXT, 
    FOREIGN KEY(camera_feed_id) REFERENCES CameraFeeds(id)
);

-- Navigation Module
CREATE TABLE NavigationRoutes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_point TEXT,
    end_point TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Collision Avoidance Detection
CREATE TABLE CollisionEvents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    severity INTEGER,
    description TEXT
);

-- Monitoring
CREATE TABLE SystemHealth (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    component TEXT,
    status TEXT,
    notes TEXT
);
