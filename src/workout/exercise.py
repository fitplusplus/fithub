from enum import Enum, auto

class MuscleGroup(Enum):
    UPPERBODY = auto()
    LOWERBODY = auto()
    TOTALBODY = auto()

muscleGroupMapping = {
    "upperbody" : MuscleGroup.UPPERBODY,
    "lowerbody" : MuscleGroup.LOWERBODY,
    "totalbody" : MuscleGroup.TOTALBODY
}

class Intensity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

intensityMapping = {
    "low" : Intensity.LOW,
    "medium" : Intensity.MEDIUM,
    "high" : Intensity.HIGH 
}

class Exercise:
    def __init__(self, name, intensity, muscle_group, description, link):
        self.name = name
        self.intensity = intensityMapping[intensity]
        self.muscle_group = muscleGroupMapping[muscle_group]
        self.description = description
        self.link = link  

    def __str__(self):
        return "WIP"

    @property
    def reps(self):
        intensityToReps = {
            Intensity.LOW : 6, 
            Intensity.MEDIUM : 10,
            Intensity.HIGH : 15
        }
        return intensityToReps[self.intensity]
