from flask import Flask, request, jsonify
from src.workout.workout_factory import *

app = Flask(__name__)

@app.route('/workout')
def get_workouts():
    wf = WorkoutFactory('src/workout/workout_data.yml')