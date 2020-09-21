import pytest

from src.workout.workout_factory import *

DATA_FILE="src/workout_data.yml"

def test_read_data_file():
    data = WorkoutFactory(DATA_FILE)
    array = data.read_exercises(DATA_FILE)
    assert array
    names = list(map(lambda x: x["name"], array))
    assert names == ['plank', 'squat', 'pushup', 'mountainclimber', 'superman', 'burpee', 'jumpingjack']    

