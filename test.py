import random
import requests

def randomize(min, max):
    value = round(random.random() * (max - min) + min, 1)
    return value

while True:
    question = input('Hello, world!')
    data = []
    data.append(randomize(2000, 3000))
    data.append(randomize(10, 30))
    data.append(randomize(40, 80))
    data.append(randomize(1, 10))
    data.append(randomize(50, 110))

    url = 'http://localhost:7801/create/EnvSensor?robot_id=sp0002&light={0}&temperature={1}&humidity={2}&carbon_monoxide={3}&noise={4}'.format(data[0], data[1], data[2], data[3], data[4])
    response = requests.get(url)
