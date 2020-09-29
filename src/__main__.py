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
    exercises = factory.create_workout(
        intensityMapping[intensity], muscleGroupMapping[muscle_group])
    return exercises


if __name__ == "__main__":
    fire.Fire(init)
