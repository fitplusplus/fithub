from enum import Enum, auto
import yaml 
from src.workout.exercise  import *


class WorkoutFactory:
    def __init__(self, path_file):
        def extract_exercises(e):
            return Exercise(e["name"], e["intensity"], e["muscle_group"], e["description"], e["link"])
            
        array = self.read_exercises(path_file)
        self.exercises = list(map(extract_exercises, array))

    def create_workout(self, muscle_group, intensity, duration):
        pass

    def filter_by_intensity(self, intensity):
       return list(filter(lambda x: x.intensity == intensity , self.exercises))

    def filter_by_muscle_group(self, muscle_group):
        return list(filter(lambda x: x.muscle_group == muscle_group , self.exercises))

    def read_exercises(self, path_file):
        a_yaml_file = open(path_file)
        parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader).get("exercises")
        return parsed_yaml_file

# see https://towardsdatascience.com/a-simple-way-to-create-python-cli-app-1a4492c164b6
# to create the CLI
