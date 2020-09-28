from enum import Enum, auto
import yaml
from src.workout.exercise import *


class WorkoutFactory:
    def __init__(self, path_file):
        def extract_exercises(e):
            return Exercise(e["name"], e["intensity"], e["muscle_group"], e["description"], e["link"])

        array = self.read_exercises(path_file)
        self.exercises = list(map(extract_exercises, array))

    def create_workout(self, intensity, muscle_group):
        exercises = self.filter_by_intensity(intensity)
        exercises = self.filter_by_muscle_group(muscle_group, exercises)
        return exercises

    def filter_by_intensity(self, intensity, exercises=[]):
        return list(filter(lambda x: x.intensity == intensity, exercises or self.exercises))

    def filter_by_muscle_group(self, muscle_group, exercises=[]):
        return list(filter(lambda x: x.muscle_group == muscle_group, exercises or self.exercises))

    def read_exercises(self, path_file):
        a_yaml_file = open(path_file)
        parsed_yaml_file = yaml.load(
            a_yaml_file, Loader=yaml.FullLoader).get("exercises")
        return parsed_yaml_file
