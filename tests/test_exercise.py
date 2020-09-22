import pytest

from src.workout.exercise import *

def test_constructor():
    ex = Exercise("chaturanga", "medium", "upperbody", "descp", "somelink")

    assert ex.name == "chaturanga"
    assert ex.intensity == Intensity.MEDIUM
    assert ex.muscle_group == MuscleGroup.UPPERBODY


def test_rep():
    ex = Exercise("chaturanga", "medium", "upperbody", "descp", "somelink")
    assert ex.reps == 10


