import pytest

from src.workout.workout_factory import *

DATA_FILE="src/workout_data.yml"

def test_read_data_file():
    data = WorkoutFactory(DATA_FILE)
    array = data.read_exercises(DATA_FILE)
    assert array
    names = list(map(lambda x: x["name"], array))
    assert names == ['plank', 'squat', 'pushup', 'mountainclimber', 'superman', 'burpee', 'jumpingjack']    

def test_constructor():
    array = WorkoutFactory(DATA_FILE).exercises
    assert array
    
    names = list(map(lambda x: x.name, array))
    assert names == ['plank', 'squat', 'pushup', 'mountainclimber', 'superman', 'burpee', 'jumpingjack']    

    intensities = list(map(lambda x : x.intensity, array))
    assert intensities == [Intensity.HIGH, Intensity.LOW, Intensity.HIGH, Intensity.MEDIUM, Intensity.LOW, Intensity.HIGH, Intensity.MEDIUM]

    muscle_groups = list(map(lambda x : x.muscle_group, array))
    assert muscle_groups == [MuscleGroup.UPPERBODY, MuscleGroup.LOWERBODY, MuscleGroup.UPPERBODY, MuscleGroup.TOTALBODY, MuscleGroup.UPPERBODY, MuscleGroup.TOTALBODY, MuscleGroup.TOTALBODY]

def test_filter_by_intensity():
    data = WorkoutFactory(DATA_FILE)
    filtered_exercises = data.filter_by_intensity(Intensity.LOW) 
    names = list(map(lambda x: x.name, filtered_exercises))
    assert names == ['squat', 'superman']

def test_filter_by_muscle_group():
    data = WorkoutFactory(DATA_FILE)
    filtered_exercises = data.filter_by_muscle_group(MuscleGroup.TOTALBODY) 
    names = list(map(lambda x: x.name, filtered_exercises))
    assert names == ['mountainclimber', 'burpee', 'jumpingjack']
    