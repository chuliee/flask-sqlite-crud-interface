table = { # Table name {column: type}
    'Users': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT NOT NULL',
        'password': 'TEXT NOT NULL'
    },
    'EnvSensor': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'robot_id': 'TEXT NOT NULL',
        'lux': 'REAL',
        'temperature': 'REAL',
        'humidity': 'REAL',
        'noise': 'REAL',
        'air_quality': 'REAL'
    }
}

## QUERY SAMPLE
# 'CREATE TABLE EnvSensor (id INTEGER PRIMARY KEY AUTOINCREMENT, robot_id TEXT NOT NULL, lux REAL, temperature REAL, humidity REAL, noise REAL, co REAL);'
# 'INSERT INTO EnvSensor(robot_id, lux, temperature, humidity, noise, co) VALUES ("sp0002", 15123.2, 11.2, 54, 114.2, 3.3);'