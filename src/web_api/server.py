from flask import Flask, request, jsonify
from src.workout.workout_factory import *
from src.workout.exercise import *
app = Flask(__name__)

@app.route('/workout')
def get_workouts():
    wf = WorkoutFactory('src/workout_data.yml')
    intensity = intensityMapping[request.args.get('intensity')]
    muscle_group = muscleGroupMapping[request.args.get('musclegroup')]
    return jsonify({"exercises": wf.create_workout(intensity, muscle_group).exercises.__str__()})