import pytest

from src.workout.workout import *
from src.workout.exercise import *

def test_constructor():
    ex1 = Exercise("chaturanga", "medium", "upperbody", "descp", "somelink")
    ex2 = Exercise("hspu", "high", "totalbody", "descp", "somelink")
    ex3 = Exercise("jump", "low", "lowerbody", "descp", "somelink")
    exercises = [ex1, ex2, ex3]
    wo = Workout(Intensity.HIGH, MuscleGroup.TOTALBODY, exercises)

    assert wo.intensity == Intensity.HIGH
    assert wo.muscle_group == MuscleGroup.TOTALBODY
    assert wo.exercises == exercises
