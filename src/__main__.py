import fire

from src.workout.workout_factory import *
from src.workout.exercise import *


def init(intensity: str, muscle_group: str):
    """
    Returns a workout
    :param intensity: intensity
    :param muscle_group: muscle group
    :return: workout based on intensity and muscle group
    """
    factory = WorkoutFactory("./src/workout_data.yml")
    work = factory.create_workout(
        intensityMapping[intensity], muscleGroupMapping[muscle_group])
    return work

def random():
    """
    Returns a workout
    :param intensity: intensity
    :param muscle_group: muscle group
    :return: workout based on intensity and muscle group
    """
    factory = WorkoutFactory("./src/workout_data.yml")
    random_work = factory.create_random_workout()
    return random_work

if __name__ == "__main__":
    fire.Fire()
