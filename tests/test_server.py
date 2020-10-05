from src.web_api import server
import json
def test_workout():
    client = server.app.test_client()
    request = client.get('/workout?intensity=high&musclegroup=totalbody')
    exercises = json.loads(request.data)["exercises"]
    assert exercises
    assert 'burpee' in exercises