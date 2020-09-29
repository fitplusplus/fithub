class Workout:

    def __init__(self, intensity, muscle_group, exercises):
        self.intensity = intensity
        self.muscle_group = muscle_group
        self.exercises = exercises

    def __str__(self):
        header= 'Intensity: {}, \nMuscle Group: {}'.format(self.intensity, self.muscle_group)
        ex = "" 
        for i in self.exercises:
            ex += '\nExercise: {}'.format(i)

        return header + ex 
