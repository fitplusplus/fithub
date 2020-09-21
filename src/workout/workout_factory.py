from enum import Enum, auto


class MuscleGroup(Enum):
    UPPERBODY = auto()
    LOWERBODY = auto()
    TOTALBODY = auto()


class Intensity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Duration(Enum):
    SHORT = auto()
    MEDIUM = auto()
    LONG = auto()


class WorkoutFactory:
    def __init__(self):
        self.workouts = []
        pass

    def create_workout(self, muscle_group, intensity, duration):
        pass

    def filter_by_intensity(self):
        pass

    def filter_by_muscle_group(self):
        pass

    def read_data_file(self, path_file):
        pass

# see https://towardsdatascience.com/a-simple-way-to-create-python-cli-app-1a4492c164b6
# to create the CLI
