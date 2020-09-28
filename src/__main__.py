import fire

from src.workout.workout_factory import *


def init(intensity: str, muscle_group: str):
    """
    Returns a workout
    :param intensity: intensity
    :param muscle_group: muscle group
    :return: workout based on intensity and muscle group
    """
    factory = WorkoutFactory("./src/workout_data.yml")
    return factory.create_workout(intensity, muscle_group)


if __name__ == "__main__":
    fire.Fire(init)
