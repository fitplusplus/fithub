from enum import Enum, auto
import yaml 

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
    def __init__(self, path_file):
        self.workouts = []
        self.read_exercises(path_file)
    

    def create_workout(self, muscle_group, intensity, duration):
        pass

    def filter_by_intensity(self):
        pass

    def filter_by_muscle_group(self):
        pass

    def read_exercises(self, path_file):
        a_yaml_file = open(path_file)
        parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader).get("exercises")
        return parsed_yaml_file

# see https://towardsdatascience.com/a-simple-way-to-create-python-cli-app-1a4492c164b6
# to create the CLI
